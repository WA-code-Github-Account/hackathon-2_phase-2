import subprocess
import time
import requests
import threading

def run_server():
    """Run the server in a subprocess"""
    import os
    os.chdir(r"D:\Projects\Hackhathon---2\Phase 2 (Todo Full Stack)\backend")
    import sys
    from app.main import app
    import uvicorn
    uvicorn.run(app, host='127.0.0.1', port=8000)

def test_api():
    """Test the API after a delay"""
    time.sleep(3)  # Wait for server to start
    
    print("Testing health endpoint...")
    try:
        response = requests.get('http://127.0.0.1:8000/health', timeout=5)
        print(f"Health Status: {response.status_code}")
        print(f"Health Response: {response.text}")
    except Exception as e:
        print(f"Health check failed: {e}")
    
    print("\nTesting signup endpoint...")
    try:
        signup_data = {
            'email': 'test@example.com',
            'name': 'Test User',
            'password': 'password123'
        }
        response = requests.post('http://127.0.0.1:8000/api/auth/sign-up', json=signup_data, timeout=10)
        print(f"Signup Status: {response.status_code}")
        print(f"Signup Response: {response.text}")
    except Exception as e:
        print(f"Signup failed: {e}")

if __name__ == "__main__":
    # Start server in a thread
    server_thread = threading.Thread(target=run_server, daemon=True)
    server_thread.start()
    
    # Wait for server to start and then test
    test_api()
    
    # Keep the main thread alive for a bit to see server output
    time.sleep(10)