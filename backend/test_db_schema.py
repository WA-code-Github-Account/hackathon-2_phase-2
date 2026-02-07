import asyncio
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy import text
from app.core.config import settings

async def check_tables():
    database_url = settings.DATABASE_URL
    if database_url.startswith("postgres://"):
        database_url = database_url.replace("postgres://", "postgresql+asyncpg://", 1)
    elif database_url.startswith("postgresql://"):
        database_url = database_url.replace("postgresql://", "postgresql+asyncpg://", 1)

    engine = create_async_engine(
        database_url,
        connect_args={"ssl": "require"}
    )
    
    async with engine.connect() as conn:
        # Query to list all tables in the current schema
        result = await conn.execute(text("""
            SELECT table_name 
            FROM information_schema.tables 
            WHERE table_schema = 'public'
        """))
        
        tables = result.fetchall()
        print("Tables in database:")
        for table in tables:
            print(f"  - {table[0]}")
            
        # Check columns in the 'user' table if it exists
        if ('user',) in tables or ('users',) in tables:
            table_name = 'user' if ('user',) in tables else 'users'
            print(f"\nColumns in '{table_name}' table:")
            result = await conn.execute(text(f"""
                SELECT column_name, data_type
                FROM information_schema.columns
                WHERE table_name = '{table_name}'
                ORDER BY ordinal_position
            """))

            columns = result.fetchall()
            for col in columns:
                print(f"  - {col[0]} ({col[1]})")

        # Check columns in the 'task' table if it exists
        if ('task',) in tables or ('todos',) in tables:
            table_name = 'task' if ('task',) in tables else 'todos'
            print(f"\nColumns in '{table_name}' table:")
            result = await conn.execute(text(f"""
                SELECT column_name, data_type
                FROM information_schema.columns
                WHERE table_name = '{table_name}'
                ORDER BY ordinal_position
            """))

            columns = result.fetchall()
            for col in columns:
                print(f"  - {col[0]} ({col[1]})")

if __name__ == "__main__":
    asyncio.run(check_tables())