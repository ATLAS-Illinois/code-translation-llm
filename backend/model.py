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

    def generate_summary(self, text, prompt="Summarize this document"):
        headers = {"Content-Type": "application/json"}
        payload = {"prompt": f"{prompt}\n\n{text}"}
        
        response = requests.post(self.url, headers=headers, data=json.dumps(payload), auth=self.auth)
        
        if response.status_code == 200:
            result = response.json()
            return result.get("text", "")
        else:
            raise Exception(f"Request failed with status {response.status_code}: {response.text}")
    
    def get_embeddings(self, text):
        headers = {"Content-Type": "application/json"}
        payload = {"text": text}
        
        response = requests.post(f"{self.url}/embeddings", headers=headers, data=json.dumps(payload), auth=self.auth)
        
        if response.status_code == 200:
            result = response.json()
            return result.get("content", []) 
        else:
            raise Exception(f"Request failed with status {response.status_code}: {response.text}")
        