import streamlit as st
import pandas as pd
import os
from datetime import datetime
from services.web_scraper.usecases import BooksUsecase

st.set_page_config(layout="wide")
st.title("📚 Web Scraper – Books to Scrape")

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

        os.makedirs("tmp", exist_ok=True)
        file_name = os.path.join(
            "tmp", f"books_{datetime.now().strftime('%Y%m%d%H%M%S')}.xlsx"
        )
        df.to_excel(file_name, index=False)

        with open(file_name, "rb") as f:
            st.download_button(
                label="⬇️ Download Excel",
                data=f,
                file_name="books.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )
    else:
        st.info("Click a button to fetch books.")

# ============================================================
#                    ABOUT (RIGHT)
# ============================================================
with col2:
    st.markdown("### About this project")

    st.markdown(
        """
        Python-based **web scraping project** using *Books to Scrape*.

        **Features**
        - Random book discovery
        - Top-rated (5⭐) books
        - Export to Excel

        **Tech stack**
        - Python
        - Requests
        - BeautifulSoup
        - FastAPI
        - Streamlit
        """
    )

    st.divider()
    st.video("https://www.youtube.com/watch?v=sF80I-TQiW0")
