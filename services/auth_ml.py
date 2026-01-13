import requests
import json
import os
from datetime import datetime, timedelta

CLIENT_ID = os.getenv("ML_CLIENT_ID")
CLIENT_SECRET = os.getenv("ML_CLIENT_SECRET")
TOKEN_URL = "https://api.mercadolibre.com/oauth/token"

# Apunta al ml_token.json en la raíz del proyecto
TOKEN_FILE = os.path.join(os.path.dirname(os.path.dirname(__file__)), "ml_token.json")


def load_tokens():
    if not os.path.exists(TOKEN_FILE):
        return None
    with open(TOKEN_FILE, "r") as f:
        return json.load(f)


def save_tokens(data):
    data["expires_at"] = (
        datetime.now() + timedelta(seconds=data["expires_in"] - 60)
    ).isoformat()
    with open(TOKEN_FILE, "w") as f:
        json.dump(data, f)


def refresh_access_token():
    tokens = load_tokens()

    if not tokens:
        raise RuntimeError("No hay refresh_token")
    payload = {
        "grant_type": "refresh_token",
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "refresh_token": tokens["refresh_token"],
    }
    
    r = requests.post(TOKEN_URL, data=payload, timeout=10)
    print(f"DEBUG response status: {r.status_code}, {r.text}")
    r.raise_for_status()
    data = r.json()
    save_tokens(data)
    
    return data["access_token"]


def get_access_token():
    tokens = load_tokens()
    if not tokens:
        raise RuntimeError("No hay tokens")
    
    if "expires_at" not in tokens:
        save_tokens(tokens)
        tokens = load_tokens()
    
    if datetime.fromisoformat(tokens["expires_at"]) > datetime.now():
        return tokens["access_token"]
    
    return refresh_access_token()