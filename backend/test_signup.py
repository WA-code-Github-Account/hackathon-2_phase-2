import requests
import time
import json

# Wait for server to be ready
time.sleep(2)

print("Testing signup endpoint...")
try:
    response = requests.post('http://127.0.0.1:8000/api/auth/sign-up', 
                           json={'email': 'test@example.com', 'name': 'Test User', 'password': 'password123'},
                           timeout=10)
    print(f"Status Code: {response.status_code}")
    print(f"Response Text: {response.text}")
    
    if response.status_code == 200:
        data = response.json()
        print(f"Token received: {len(data.get('token', '')) > 0}")
        
        # Test tasks endpoint with token
        headers = {'Authorization': f'Bearer {data.get("token")}'}
        tasks_response = requests.get('http://127.0.0.1:8000/api/tasks/', headers=headers, timeout=10)
        print(f"Tasks Status: {tasks_response.status_code}")
        print(f"Tasks Response: {tasks_response.text}")
    else:
        print("Signup failed")
        
except requests.exceptions.Timeout:
    print("Request timed out")
except requests.exceptions.RequestException as e:
    print(f"Request failed: {e}")