import os
import json
import requests
from dotenv import load_dotenv
from requests.auth import HTTPBasicAuth

load_dotenv()

class RemoteModelLoader:
    def __init__(self):
        self.url = os.getenv("LLM_URL")
        self.auth = HTTPBasicAuth(os.getenv("LLM_USERNAME"), os.getenv("LLM_PASSWORD"))

    def generate_code(self, prompt):
       
        headers = {"Content-Type": "application/json"}
        payload = {"prompt": prompt}

        response = requests.post(self.url, headers=headers, data=json.dumps(payload), auth=self.auth)

        if response.status_code == 200:
            result = response.json()
            return result.get("content", "").strip()
        else:
            raise Exception(f"Request failed with status {response.status_code}: {response.text}")
