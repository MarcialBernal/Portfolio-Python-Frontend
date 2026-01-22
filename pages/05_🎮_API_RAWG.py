import streamlit as st
import pandas as pd
import time
from services.api_consumption.usecases import RawgGenresUsecase

####
st.set_page_config(page_title="RAWG API CONSUMPTION",page_icon="🎮", layout="wide")

title_placeholder = st.empty()
title_text = "🎮 RAWG API CONSUMPTION"

if "rawg_title_done" not in st.session_state:
    st.session_state["rawg_title_done"] = False

if not st.session_state["rawg_title_done"]:
    for i in range(1, len(title_text) + 1):
        title_placeholder.markdown(f"# {title_text[:i]}")
        time.sleep(0.03)
    st.session_state["rawg_title_done"] = True
else:
    title_placeholder.markdown(f"# {title_text}")
   
    
####
with st.spinner("Loading data from RAWG..."):
    usecase = RawgGenresUsecase()
    data = usecase.list_genres()
    

####
col_1, col_2 = st.columns([1, 1])

usecase = RawgGenresUsecase()
data = usecase.list_genres()

with col_1:
    st.subheader("🎯 Genres Overview")
    cols = st.columns(5)
    for i, genre in enumerate(data["results"]):
        with cols[i % 5]:
            st.metric(
                label=f"{genre['name']}",
                value=f"{genre['games_count']:,}",
                help="Number of games available in this genre"
            )
with col_2:
    st.subheader("About this project")
    st.markdown(
        '''This project consumes the RAWG API through a FastAPI backend that I built  
        to demonstrate my ability to integrate and work with third-party APIs.  
        It focuses on fetching real-time external data and transforming it into meaningful visualizations.'''
    )