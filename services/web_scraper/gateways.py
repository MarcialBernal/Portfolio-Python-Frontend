import requests
import os

BASE_URL = os.getenv("SCRAPER_API_URL", "http://localhost:8000/webscraper")

# ============================================================
#                         BOOKS
# ============================================================
class BooksGateway:
    def __init__(self):
        self.base_url = BASE_URL

    def get_random_books(self, limit: int = 10):
        r = requests.get(f"{self.base_url}/books/random", params={"limit": limit})
        r.raise_for_status()
        return r.json()

    def get_top_books(self, limit: int = 10):
        r = requests.get(f"{self.base_url}/books/top", params={"limit": limit})
        r.raise_for_status()
        return r.json()