import streamlit as st
import pandas as pd
import io
import time
from ui.sidebar import render_sidebar

render_sidebar()


@st.cache_data
def file_converter(file):
    df = pd.read_excel(file, engine="openpyxl")
    return df.to_csv(index=False).encode("utf-8")

st.set_page_config(page_title="Excel Converter", page_icon="📄", layout="wide")

title_placeholder = st.empty()
title_text = "📄 Excel to CSV Converter"

if "converter_title_done" not in st.session_state:
    st.session_state["converter_title_done"] = False

if not st.session_state["converter_title_done"]:
    for i in range(1, len(title_text) + 1):
        title_placeholder.markdown(f"# {title_text[:i]}")
        time.sleep(0.03)
    st.session_state["converter_title_done"] = True
else:
    title_placeholder.markdown(f"# {title_text}")


####
col1, col2 = st.columns([1, 2])

with col1:
    uploaded_file = st.file_uploader("Upload an Excel file", type=["xlsx"])

    if uploaded_file:
        st.success(f"File '{uploaded_file.name}' uploaded successfully!")

        if st.button("Convert to CSV"):
            try:
                csv = file_converter(uploaded_file)
                preview = pd.read_csv(io.BytesIO(csv))

                st.write("✅ File Preview:")
                st.dataframe(preview.head())

                st.download_button(
                    label="⬇️ Download CSV file",
                    data=csv,
                    file_name=uploaded_file.name.replace(".xlsx", ".csv"),
                    mime="text/csv"
                )
            except Exception as e:
                st.error("An error has occurred while converting the file.")
                st.exception(e)


# ---- Right column (About) ----
with col2:
    st.subheader("About this project")
    st.markdown("""
                This is a simple utility that converts Excel files (.xlsx) into CSV format using Pandas.

                Users upload an Excel file, preview the converted data, and download the resulting CSV instantly.  
                The project focuses on clean data handling, fast file processing,  
                and a minimal user interface for everyday data conversion tasks.
                """)