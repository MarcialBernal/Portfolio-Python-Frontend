import streamlit as st
import pandas as pd
import os
from datetime import datetime
from services.web_scraper.usecases import ScraperUsecase

st.set_page_config(layout="wide")
st.title('WEB SCRAPER Mercado Libre')

scraper_uc = ScraperUsecase()

col1, col2 = st.columns([3,4])

with col1:
    search_query = st.text_input("Input an item to search on Mercado Libre:")

    if search_query:
        st.write(f"Search results for: {search_query}")

        data = scraper_uc.search_items(search_query)

        if data:
            df = pd.DataFrame(data)

            # Guardar Excel temporalmente
            os.makedirs("tmp", exist_ok=True)
            file_name = os.path.join("tmp", f"search_{datetime.now().strftime('%Y%m%d%H%M%S')}.xlsx")
            df.to_excel(file_name, index=False)

            st.dataframe(df, use_container_width=True)

            with open(file_name, "rb") as f:
                st.download_button(
                    label="⬇️ Download Excel",
                    data=f,
                    file_name="search_results.xlsx",
                    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                )

            try:
                os.remove(file_name)
            except FileNotFoundError:
                pass
        else:
            st.error("No items found")

with col2:
    st.markdown(
        """
        ### About this project
        Python-based web scraper for MercadoLibre México.

        Tech stack:
        - Python
        - Requests
        - Backend (BeautifulSoup / Selenium)
        """
    )
    st.divider()
    st.video("https://www.youtube.com/watch?v=sF80I-TQiW0")
