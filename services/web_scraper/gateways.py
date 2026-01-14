import requests
import os

BASE_URL = os.getenv("SCRAPER_API_URL", "http://localhost:8000")  

class ScraperGateway:
    def __init__(self):
        self.base_url = BASE_URL

    def search_items(self, query: str):
        try:
            r = requests.get(f"{self.base_url}/scraper?query={query}", timeout=15)
            r.raise_for_status()
            return r.json()  
        except requests.RequestException as e:
            print(f"Error calling backend: {e}")
            return []