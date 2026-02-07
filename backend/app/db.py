from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlmodel.ext.asyncio.session import AsyncSession
from .core.config import settings

from urllib.parse import urlparse, parse_qs, urlencode, urlunparse

database_url = settings.DATABASE_URL

# Handle different database types appropriately
if database_url.startswith("postgresql://") or database_url.startswith("postgres://"):
    # For PostgreSQL, transform to asyncpg and clean up query params
    # Handle both postgres:// and postgresql:// prefixes
    if database_url.startswith("postgres://"):
        database_url = database_url.replace("postgres://", "postgresql+asyncpg://", 1)
    elif database_url.startswith("postgresql://"):
        database_url = database_url.replace("postgresql://", "postgresql+asyncpg://", 1)

    # Clean up query params for asyncpg
    parsed = urlparse(database_url)
    qs = parse_qs(parsed.query)

    # Remove unsupported keys
    for key in ["sslmode", "channel_binding", "options"]:
        qs.pop(key, None)

    # Rebuild URL without forcing ssl query params; we'll pass SSL via connect_args
    new_query = urlencode(qs, doseq=True)
    database_url = urlunparse(parsed._replace(query=new_query))

    # Determine connect args: enable SSL for non-local hosts (e.g., Supabase/Neon)
    connect_args = {"ssl": "require"}  # Use string "require" which is commonly accepted
else:
    # For SQLite and other databases, use the URL as-is
    connect_args = {}

engine = create_async_engine(
    database_url,
    echo=True,
    future=True,
    connect_args=connect_args,
    pool_pre_ping=True,
    pool_recycle=300,
    pool_size=10,
    max_overflow=20
)

from sqlmodel import SQLModel

async def get_async_session() -> AsyncSession:
    async_session = sessionmaker(
        engine, class_=AsyncSession, expire_on_commit=False
    )
    async with async_session() as session:
        yield session

async def create_db_and_tables():
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)