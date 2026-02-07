import asyncio
from sqlmodel import SQLModel, Field, create_engine, Session
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine
from typing import Optional
import uuid
from datetime import datetime

# Define simplified models to test
class User(SQLModel, table=True):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()), primary_key=True)
    email: str = Field(unique=True, index=True)
    name: Optional[str] = None
    hashed_password: str

# Test creating a user directly
async def test_user_creation():
    from app.core.config import settings
    from urllib.parse import urlparse, parse_qs, urlencode, urlunparse

    database_url = settings.DATABASE_URL
    if database_url.startswith("postgres://"):
        database_url = database_url.replace("postgres://", "postgresql+asyncpg://", 1)
    elif database_url.startswith("postgresql://"):
        database_url = database_url.replace("postgresql://", "postgresql+asyncpg://", 1)

    parsed = urlparse(database_url)
    qs = parse_qs(parsed.query)

    for key in ["sslmode", "channel_binding", "options"]:
        qs.pop(key, None)

    new_query = urlencode(qs, doseq=True)
    database_url = urlunparse(parsed._replace(query=new_query))

    engine = create_async_engine(
        database_url,
        echo=True,
        connect_args={"ssl": "require"}
    )
    
    # Create tables
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)
    
    # Create a user
    from passlib.context import CryptContext
    pwd_context = CryptContext(schemes=["pbkdf2_sha256"], deprecated="auto")
    
    def get_password_hash(password):
        return pwd_context.hash(password)
    
    async with AsyncSession(engine) as session:
        user = User(
            email="test@example.com",
            name="Test User",
            hashed_password=get_password_hash("password123")
        )
        session.add(user)
        await session.commit()
        await session.refresh(user)
        print(f"User created successfully with ID: {user.id}")
        return user

if __name__ == "__main__":
    user = asyncio.run(test_user_creation())
    print("Test completed successfully!")