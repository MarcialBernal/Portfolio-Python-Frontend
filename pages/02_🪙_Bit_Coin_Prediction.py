import streamlit as st
import time
from ui.sidebar import render_sidebar
from services.auto_ml.usecases import AutoMLPredictionUsecase

render_sidebar()

st.set_page_config(page_title="Bitcoin Prediction", page_icon="🪙", layout="wide")

usecase = AutoMLPredictionUsecase()

# ---------------- TITLE ----------------
title_placeholder = st.empty()
title_text = "🪙 Bitcoin Next-Day Prediction"

if "btc_title_done" not in st.session_state:
    st.session_state["btc_title_done"] = False

if not st.session_state["btc_title_done"]:
    for i in range(1, len(title_text) + 1):
        title_placeholder.markdown(f"# {title_text[:i]}")
        time.sleep(0.03)
    st.session_state["btc_title_done"] = True
else:
    title_placeholder.markdown(f"# {title_text}")

# ---------------- LAYOUT ----------------
col1, col2 = st.columns([1, 2])

# -------- LEFT COLUMN (APP) --------
with col1:
    st.subheader("Run prediction")

    if st.button("🔮 Predict next day trend"):
        with st.spinner("Running model..."):
            result = usecase.get_prediction()

        st.success("Prediction completed!")

        st.metric("📅 Date", result["date"])
        st.metric("📈 Trend", result["trend"])
        st.metric("🎯 Confidence", f"{result['confidence']*100:.2f}%")

# -------- RIGHT COLUMN (ABOUT) --------
with col2:
    st.subheader("About this project")
    st.markdown("""
    This project predicts the **next-day trend of Bitcoin (UP or DOWN)** using a machine learning pipeline.

    The system:
    - Fetches real historical price data
    - Trains a time-series classification model
    - Automatically retrains if the dataset is outdated
    - Returns both prediction and confidence score

    The frontend is built with **Streamlit**, connected to a **FastAPI backend**, and designed to demonstrate
    real-world ML system architecture — not just notebooks or static demos.
    """)
