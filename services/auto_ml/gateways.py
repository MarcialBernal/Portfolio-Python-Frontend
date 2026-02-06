import requests
import os

BASE_URL = os.getenv("AUTO_ML_API_URL", "http://localhost:8000")

# ============================================================
#                   AUTO ML
# ============================================================

class AutoMLGateway:
    def __init__(self):
        self.base_url = BASE_URL

    def get_prediction(self):
        r = requests.get(f"{self.base_url}/predict")
        r.raise_for_status()
        return r.json()
