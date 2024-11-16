import requests
from requests.auth import HTTPBasicAuth
import json
from dotenv import load_dotenv
import os

load_dotenv()

url = os.getenv("LLM_URL")
username = os.getenv("LLM_USERNAME")
password = os.getenv("LLM_PASSWORD")


payload = {
    "prompt": "Write a Hello World program in C++",
    "n_predict": -1
}
headers = {"Content-Type": "application/json"}


response = requests.post(
    url,
    headers=headers,
    data=json.dumps(payload),
    auth=HTTPBasicAuth(username, password)
)


if response.status_code == 200:
    # Parse the JSON response
    result = response.json()
    # Extract the text field from the first choice
    generated_text = result.get("choices", [])[0].get("text", "")
    # print("Generated Code:")
    # print(generated_text)
else:
    print(f"Request failed with status {response.status_code}: {response.text}")
