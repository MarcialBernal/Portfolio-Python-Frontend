import streamlit as st 
from dotenv import load_dotenv
import time
from ui.sidebar import render_sidebar

load_dotenv()

def main():
    st.set_page_config(
        page_title="Marcial Bernal",
        page_icon="🌮",
    )
    
    st.sidebar.success("Select a project above.")
    render_sidebar()

    # --- HERO ---
    if "title_done" not in st.session_state:
        st.session_state["title_done"] = False

    title_placeholder = st.empty()
    title_text = "Marcial Bernal — Python Developer 💻🐍"

    if not st.session_state["title_done"]:
        for i in range(1, len(title_text) + 1):
            title_placeholder.markdown(f"# {title_text[:i]}")
            time.sleep(0.03)
        st.session_state["title_done"] = True
    else:
        title_placeholder.markdown(f"# {title_text}")

    st.caption(
        "Python developer focused on REST APIs, automation, data workflows, "
        "machine learning, and generative AI systems."
    )

    st.divider()

    # --- SKILL FILTERS ---
    st.subheader("🧰 Explore by Skill")
    skills = [
        "🤖 Machine Learning",
        "📊 Data Analysis",
        "🌐 API Consumption",
        "⚙️ Automation",
        "✨ Generative AI",
        "🕷️ Web Scraping",
        "🔌 REST APIs",
    ]

    skill_to_pages = {
        "🤖 Machine Learning": [],
        "📊 Data Analysis": ["pages/04_📊_Data_Visualization.py"],
        "🌐 API Consumption": [
            "pages/01_🏋️_Gym_Assistant.py",
            "pages/05_🎮_API_RAWG.py",
        ],
        "⚙️ Automation": [
            "pages/01_🏋️_Gym_Assistant.py",
            "pages/06_📄_File_Converter.py",
        ],
        "✨ Generative AI": ["pages/01_🏋️_Gym_Assistant.py"],
        "🕷️ Web Scraping": ["pages/03_📚_Web Scraper – Books to Scrape.py"],
        "🔌 REST APIs": [
            "pages/01_🏋️_Gym_Assistant.py",
            "pages/02_📦_Warehouse.py",
            "pages/05_🎮_API_RAWG.py",
        ],
    }

    page_labels = {
        "pages/01_🏋️_Gym_Assistant.py": "🏋️ Gym Assistant",
        "pages/02_📦_Warehouse.py": "📦 Warehouse",
        "pages/03_📚_Web Scraper – Books to Scrape.py": "📚 Web Scraper – Books to Scrape",
        "pages/04_📊_Data_Visualization.py": "📊 Data Visualization",
        "pages/05_🎮_API_RAWG.py": "🎮 RAWG API Explorer",
        "pages/06_📄_File_Converter.py": "📄 File Converter",
    }

    selected_skill = None
    cols = st.columns(len(skills))
    for col, skill in zip(cols, skills):
        with col:
            if st.button(skill, width="stretch"):
                selected_skill = skill

    # --- PROJECT LINKS ---
    if selected_skill:
        st.divider()
        st.subheader(f"Projects using {selected_skill}")
        for page in skill_to_pages[selected_skill]:
            st.page_link(page, label=page_labels[page], icon="➡️")

    st.divider()

    # --- ABOUT ME - ABOUT PORTFOLIO  ---
    st.subheader("🍳 About Me")
    st.markdown("""
    Before diving into code, I spent 10 years as a chef in Mexico 🌵 — a career that shaped my creativity, precision, and attention to detail.  
    Today, I bring that same mindset to software development, building real-world tools and internal systems for a construction company while continuously expanding my skills through personal projects.

    The 🌮 in my logo represents my roots and my approach to coding: craft, experimentation, and continuous improvement.
    """)

    st.divider()

    st.subheader("🏗️ About This Portfolio")
    st.markdown("""
    This portfolio is not just a collection of projects — it’s a real product.

    I built a full backend with FastAPI, deployed it to the cloud, and connected it to real external APIs to work with live data, not mock examples. The frontend runs on Streamlit so I can turn ideas into working tools quickly.

    The goal isn’t just to show code, but to show how I design systems, integrate third-party services, and turn raw data into something useful, interactive, and real.
    """)


if __name__ == "__main__":
    main()
