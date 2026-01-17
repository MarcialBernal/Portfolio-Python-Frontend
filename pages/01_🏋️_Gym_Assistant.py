import streamlit as st
import time
from services.gym_assistant.assistant_client import AssistantClient  
from ui.sidebar import render_sidebar

render_sidebar()

st.set_page_config(page_title="Gym Assistant Chat",page_icon="🏋️", layout="wide")
assistant = AssistantClient()

title_placeholder = st.empty()
title_text = "🏋️ Gym Assistant"

for i in range(1, len(title_text) + 1):
    title_placeholder.markdown(f"# {title_text[:i]}")
    time.sleep(0.03)


col1, col2 = st.columns([1, 1])

with col1:
    if "messages" not in st.session_state:
        st.session_state.messages = []

    chat_container = st.container()
    user_input = st.chat_input("Write a message…")

    if user_input:
        st.session_state.messages.append({"role": "user", "content": user_input})

        with chat_container:
            with st.chat_message("user"):
                st.write(user_input)

        with st.spinner(
            "Connecting to AI model... First request may take ~50 seconds due to backend cold start. Thanks for your patience."
        ):
            reply = assistant.chat(st.session_state.messages)

        st.session_state.messages.append({"role": "assistant", "content": reply})
        st.rerun()

    with chat_container:
        for msg in st.session_state.messages:
            with st.chat_message(msg["role"]):
                st.write(msg["content"])

with col2:
    st.subheader("About this project")
    st.markdown("""
                This application is an AI-powered gym assistant  
                that generates personalized workout routines based on user information  
                such as age, height, weight, fitness goals, and weekly availability.

                    User data is stored in a database, 
                    allowing the assistant to recognize returning users, 
                    retrieve their previous routines, 
                    and modify them when goals or preferences change. 
                    Through natural conversation, 
                    users can review their routines, 
                    update their information, or request new training plans.

                The system uses a Streamlit front-end connected to a FastAPI backend hosted on Render,   
                which integrates an OpenAI-powered assistant to handle the conversational logic and decision-making.
                """)

    
    
    st.divider()
    st.video("https://www.youtube.com/watch?v=sF80I-TQiW0")


