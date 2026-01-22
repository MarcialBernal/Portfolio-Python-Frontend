import streamlit as st
import pandas as pd
import io
import time
from datetime import datetime
from services.web_scraper.usecases import BooksUsecase
from ui.sidebar import render_sidebar

render_sidebar()


st.set_page_config(page_title="Web Scraper",page_icon="📚", layout="wide")

title_placeholder = st.empty()
title_text = "📚 Web Scraper – Books to Scrape"

if "scraper_title_done" not in st.session_state:
    st.session_state["scraper_title_done"] = False

if not st.session_state["scraper_title_done"]:
    for i in range(1, len(title_text) + 1):
        title_placeholder.markdown(f"# {title_text[:i]}")
        time.sleep(0.03)
    st.session_state["scraper_title_done"] = True
else:
    title_placeholder.markdown(f"# {title_text}")


####
books_uc = BooksUsecase()

col1, col2 = st.columns([3, 2])

# ============================================================
#                    SCRAPER (LEFT)
# ============================================================
with col1:
    st.markdown("### Scraper")

    st.markdown(
        """
        **Random Books**  
        Returns a random selection of books from the website.

        **Top Popular Books**  
        Returns only books with ⭐⭐⭐⭐⭐ rating.
        """
    )

    limit = st.slider("Number of books", min_value=5, max_value=50, value=10)

    if st.button("🎲 Get Random Books"):
        st.session_state["data"] = books_uc.list_random_books(limit=limit)

    if st.button("🔥 Get Top Popular Books"):
        st.session_state["data"] = books_uc.list_top_books(limit=limit)

    st.divider()
    st.markdown("### Results")

    if "data" in st.session_state and st.session_state["data"]:
        df = pd.DataFrame(st.session_state["data"])
        st.dataframe(df, use_container_width=True)

        buffer = io.BytesIO()
        with pd.ExcelWriter(buffer, engine="openpyxl") as writer:
            df.to_excel(writer, index=False)
        buffer.seek(0)

        st.download_button(
            label="⬇️ Download Excel",
            data=buffer,
            file_name="books.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )
    else:
        st.info("Click a button to fetch books.")

# ============================================================
#                    ABOUT (RIGHT)
# ============================================================
with col2:
    st.subheader("About this project")
    st.markdown("""
                This is a Python-based web scraping project that collects data from the *Books to Scrape* website using BeautifulSoup.  
                The scraper extracts information such as book title, price, image URL, book URL, rating, and availability.  

                It can generate a list of random books with their details, and it also provides a list of top-rated books (5⭐) as recommendations.

                The project features a Streamlit front-end connected to a FastAPI backend hosted on Render.  
                The front-end interacts with the backend through endpoints that trigger the scraping script and return the results to the user.
                """)

    st.divider()
    st.video("https://www.youtube.com/watch?v=sF80I-TQiW0")
