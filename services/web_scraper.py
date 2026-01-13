import pandas as pd
import requests
from datetime import datetime
import os
from .auth_ml import get_access_token

SITE_ID = "MLM"

#######
def get_search_results(query, limit=10):
    url = f"https://api.mercadolibre.com/sites/{SITE_ID}/search"

    headers = {
        "Authorization": f"Bearer {get_access_token()}",
        "Accept": "application/json"
    }

    params = {
        "q": query,
        "limit": limit
    }

    response = requests.get(url, headers=headers, params=params, timeout=10)
    response.raise_for_status()
    return response.json().get("results", [])


#######
def parse_item(item):
    return {
        "Date": datetime.now().strftime("%Y-%m-%d"),
        "Title": item.get("title"),
        "Price": item.get("price"),
        "Original Price": item.get("original_price"),
        "Available Qty": item.get("available_quantity"),
        "Condition": item.get("condition"),
        "Category ID": item.get("category_id"),
        "Free Shipping": item.get("shipping", {}).get("free_shipping", False),
        "Image URL": item.get("thumbnail"),
        "Item URL": item.get("permalink")
    }


#######
def save_to_excel(data):
    os.makedirs("tmp", exist_ok=True)
    file_path = os.path.join("tmp", "search.xlsx")
    pd.DataFrame(data).to_excel(file_path, index=False)
    return file_path


#######
def run_scraper(search_query):
    items = get_search_results(search_query)
    data = [parse_item(item) for item in items]

    if not data:
        return pd.DataFrame(), None

    file_name = save_to_excel(data)
    return pd.DataFrame(data), file_name
