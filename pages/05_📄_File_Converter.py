import streamlit as st
import pandas as pd
import io

@st.cache_data
def file_converter(file):
    df = pd.read_excel(file, engine="openpyxl")
    return df.to_csv(index=False).encode("utf-8")

st.set_page_config(
    page_title="Excel Converter",
    page_icon="📄",
)

st.title("📄 Excel to CSV Converter")

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
