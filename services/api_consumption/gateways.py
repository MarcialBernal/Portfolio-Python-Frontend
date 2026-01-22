import requests
import os

BASE_URL = os.getenv("API_CONSUMPTION_URL", "http://localhost:8000/apiconsumption")

# ============================================================
#                         GENRES
# ============================================================
class ApiConsumptionGateway:
    def __init__(self):
        self.base_url = BASE_URL

    def get_rawg_genres(self):
        r = requests.get(f"{self.base_url}/rawg/genres")
        r.raise_for_status()
        return r.json()