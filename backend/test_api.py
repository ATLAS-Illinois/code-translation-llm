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
    "prompt": """
            
            You are a code translation assistant. Your only task is to translate C++ code into Python code.
            IMPORTANT RULES:
            - Output ONLY the translated Python code
            - Do not include any explanations
            - Do not include any comments unless they were present in the original code
            - Do not include code fence markers (```)
            - Do not include any text before or after the code
            - Preserve the original indentation style where possible
            - Maintain any existing comments from the source code
            - If the code cannot be translated, output only 'TRANSLATION_ERROR'
            
            Convert this to Python Code: 
            ```cpp
            #include <iostream>

            int main() {
                std::cout << "Hello, World!" << std::endl;
                return 0;
            }
            ```
            """,
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
    generated_text = result.get("content")
    print(generated_text)
    # print("Generated Code:")
    # print(generated_text)
else:
    print(f"Request failed with status {response.status_code}: {response.text}")
