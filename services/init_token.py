import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

CLIENT_ID = os.getenv("ML_CLIENT_ID")
CLIENT_SECRET = os.getenv("ML_CLIENT_SECRET")
REDIRECT_URI = "https://marcial-bernal-portfolio-python.streamlit.app/"
CODE = "TG-6965b711231bcf00010ca7e9-241411193"

print("CLIENT_ID:", CLIENT_ID)
print("CLIENT_SECRET:", CLIENT_SECRET)
print("REDIRECT_URI:", REDIRECT_URI)
print("CODE:", CODE)

r = requests.post(
    "https://api.mercadolibre.com/oauth/token",
    data={
        "grant_type": "authorization_code",
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "code": CODE,
        "redirect_uri": REDIRECT_URI,
    },
    headers={"Content-Type": "application/x-www-form-urlencoded"},
    timeout=10
)

r.raise_for_status()

with open("ml_token.json", "w") as f:
    json.dump(r.json(), f)

print("ml_token.json creado")
