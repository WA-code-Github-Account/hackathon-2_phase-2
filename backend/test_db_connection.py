import asyncio
from sqlalchemy.ext.asyncio import create_async_engine
from urllib.parse import urlparse
from app.core.config import settings

async def test_connection():
    database_url = settings.DATABASE_URL
    print(f"Database URL: {database_url}")
    
    # Handle PostgreSQL connection
    if database_url.startswith("postgres://"):
        database_url = database_url.replace("postgres://", "postgresql+asyncpg://", 1)
    elif database_url.startswith("postgresql://"):
        database_url = database_url.replace("postgresql://", "postgresql+asyncpg://", 1)
    
    print(f"Modified URL: {database_url}")
    
    # Parse the URL to check if it's valid
    parsed = urlparse(database_url)
    print(f"Parsed URL - Host: {parsed.hostname}, Port: {parsed.port}, User: {parsed.username}")
    
    # Create engine with SSL settings for Supabase
    engine = create_async_engine(
        database_url,
        echo=True,
        connect_args={"ssl": "require"}
    )
    
    try:
        async with engine.begin() as conn:
            result = await conn.execute("SELECT version()")
            version = result.scalar()
            print(f"Database connection successful! Version: {version}")
            return True
    except Exception as e:
        print(f"Database connection failed: {e}")
        return False
    finally:
        await engine.dispose()

if __name__ == "__main__":
    success = asyncio.run(test_connection())
    print(f"Connection test {'passed' if success else 'failed'}")