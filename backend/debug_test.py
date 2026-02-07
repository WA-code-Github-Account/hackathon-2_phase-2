#!/usr/bin/env python
"""Test script to debug the database connection issue"""

import os
import sys
from pathlib import Path

# Add the backend directory to the path
sys.path.insert(0, str(Path(__file__).parent))

# Set the environment variable explicitly
os.environ['DATABASE_URL'] = 'sqlite+aiosqlite:///todo_app.db'
os.environ['PROJECT_NAME'] = 'Todo API'
os.environ['BETTER_AUTH_SECRET'] = 'test-secret'
os.environ['BETTER_AUTH_URL'] = 'http://localhost:3000'

print("Testing individual imports...")

try:
    print("1. Testing pydantic settings...")
    from app.core.config import settings
    print(f"   Settings loaded: {settings.PROJECT_NAME}")
    print(f"   DB URL: {settings.DATABASE_URL}")
except Exception as e:
    print(f"   Error with config: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)

try:
    print("2. Testing database engine creation...")
    from app.db import engine
    print("   Database engine created successfully!")
except Exception as e:
    print(f"   Error with database: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)

try:
    print("3. Testing main app import...")
    from app.main import app
    print(f"   App loaded: {app.title}")
except Exception as e:
    print(f"   Error with main app: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)

print("All imports successful!")