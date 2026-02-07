from app.main import app
import uvicorn
import threading
import time
import requests

def make_request():
    time.sleep(3)  # Wait for server to start
    print("Making request...")
    try:
        response = requests.post('http://127.0.0.1:8000/api/auth/sign-up', 
                               json={'email': 'test6@example.com', 'name': 'Test User 6', 'password': 'password123'})
        print(f"Response: {response.status_code} - {response.text}")
    except Exception as e:
        print(f"Request failed: {e}")

# Start request in background
request_thread = threading.Thread(target=make_request)
request_thread.start()

if __name__ == '__main__':
    print("Starting server...")
    uvicorn.run(app, host='127.0.0.1', port=8000, log_level="info")