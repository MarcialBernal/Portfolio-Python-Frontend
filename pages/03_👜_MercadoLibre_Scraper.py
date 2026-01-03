import streamlit as st
import pandas as pd
import os
from services.web_scraper import run_scraper

st.set_page_config(layout="wide")
st.title('''WEB SCRAPPER Mercado Libre''')

col1, col2 = st.columns([3,4])

with col1:
    search_query = st.text_input("Input an item to search on Mercado Libre:")

    if search_query:
        st.write(f"Search results of item: {search_query}")

        df, file_name = run_scraper(search_query)

        if not df.empty:
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
        A Python-based web scraping tool that extracts product data from MercadoLibre México using a search query.

        The scraper retrieves product titles, prices, images, URLs, and fulfillment status, structures the data with Pandas, and exports the results to an Excel file.

        Built with a modular design and clean data handling, this project demonstrates practical experience with HTTP requests, HTML parsing, and data processing, and can be easily integrated into applications such as Streamlit dashboards.

        Tech stack: \n
        - Python \n
        - Requests \n
        - BeautifulSoup \n
        - Pandas
        """
        )
    st.divider()
    st.video("https://www.youtube.com/watch?v=sF80I-TQiW0")