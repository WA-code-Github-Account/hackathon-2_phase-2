import asyncio
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy import text
from app.core.config import settings
from app.models import user, task  # Import to register models
from sqlmodel import SQLModel

async def reset_database_schema():
    database_url = settings.DATABASE_URL
    if database_url.startswith("postgres://"):
        database_url = database_url.replace("postgres://", "postgresql+asyncpg://", 1)
    elif database_url.startswith("postgresql://"):
        database_url = database_url.replace("postgresql://", "postgresql+asyncpg://", 1)

    engine = create_async_engine(
        database_url,
        connect_args={"ssl": "require"}
    )
    
    print("Dropping existing tables...")
    async with engine.begin() as conn:
        # Drop all tables
        await conn.execute(text("DROP TABLE IF EXISTS task CASCADE"))
        await conn.execute(text("DROP TABLE IF EXISTS \"user\" CASCADE"))  # user is a reserved word in PostgreSQL
        await conn.execute(text("DROP TABLE IF EXISTS sessions CASCADE"))
        await conn.commit()
    
    print("Creating new tables based on models...")
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)
    
    print("Database schema reset successfully!")

if __name__ == "__main__":
    asyncio.run(reset_database_schema())