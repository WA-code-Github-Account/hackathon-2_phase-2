import requests
import json

try:
    response = requests.get('http://localhost:8000/health')
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.text}")
    print(f"JSON Response: {response.json()}")
except Exception as e:
    print(f"Error connecting to API: {e}")