import os
import requests

class AssistantClient:
    def __init__(self):
        self.url = os.getenv("ASSISTANT_API_URL")

    def chat(self, messages):
        r = requests.post(self.url, json={"messages": messages})
        r.raise_for_status()
        return r.json().get("reply", "")