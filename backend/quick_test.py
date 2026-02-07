import asyncio
import threading
import time
import requests
from app.main import app
from fastapi.testclient import TestClient

def test_with_client():
    time.sleep(2)  # Wait a bit
    print('Testing with client...')
    try:
        client = TestClient(app)
        response = client.post('/api/auth/sign-up', json={
            'email': 'test17@example.com',
            'name': 'Test User 17',
            'password': 'password123'
        })
        print(f'Response: {response.status_code} - {response.text}')
    except Exception as e:
        print(f'Test failed: {e}')
        import traceback
        traceback.print_exc()

# Start test in background
test_thread = threading.Thread(target=test_with_client)
test_thread.start()

# Just run a quick test without starting the full server
print("Running quick test...")
test_with_client()