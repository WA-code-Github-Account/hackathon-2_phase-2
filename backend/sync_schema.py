import asyncio
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy import text
from app.core.config import settings
from app.models.user import User
from sqlmodel import SQLModel

async def sync_schema():
    database_url = settings.DATABASE_URL
    if database_url.startswith("postgres://"):
        database_url = database_url.replace("postgres://", "postgresql+asyncpg://", 1)
    elif database_url.startswith("postgresql://"):
        database_url = database_url.replace("postgresql://", "postgresql+asyncpg://", 1)

    engine = create_async_engine(
        database_url,
        connect_args={"ssl": "require"}
    )
    
    # Reflect the existing table structure
    from sqlalchemy import MetaData
    meta = MetaData()
    
    async with engine.connect() as conn:
        # Get current columns in user table
        result = await conn.execute(text("""
            SELECT column_name, data_type, is_nullable
            FROM information_schema.columns 
            WHERE table_name = 'user'
            ORDER BY ordinal_position
        """))
        
        current_columns = result.fetchall()
        print("Current columns in 'user' table:")
        for col in current_columns:
            print(f"  - {col[0]} ({col[1]}, nullable={col[2]})")
        
        print("\nExpected columns from model:")
        for field_name, field in User.__fields__.items():
            print(f"  - {field_name}")
        
        # Try to add missing columns
        current_col_names = [col[0] for col in current_columns]
        
        if 'name' not in current_col_names:
            print("\nAdding 'name' column...")
            await conn.execute(text("ALTER TABLE \"user\" ADD COLUMN IF NOT EXISTS name VARCHAR"))
            await conn.commit()

        if 'updated_at' not in current_col_names:
            print("\nAdding 'updated_at' column...")
            await conn.execute(text("ALTER TABLE \"user\" ADD COLUMN IF NOT EXISTS updated_at TIMESTAMP"))
            await conn.commit()

        # Also check task table
        result = await conn.execute(text("""
            SELECT column_name, data_type, is_nullable
            FROM information_schema.columns
            WHERE table_name = 'task'
            ORDER BY ordinal_position
        """))

        task_columns = result.fetchall()
        print("\nCurrent columns in 'task' table:")
        for col in task_columns:
            print(f"  - {col[0]} ({col[1]}, nullable={col[2]})")

        task_col_names = [col[0] for col in task_columns]
        if 'updated_at' not in task_col_names:
            print("\nAdding 'updated_at' column to task table...")
            await conn.execute(text("ALTER TABLE \"task\" ADD COLUMN IF NOT EXISTS updated_at TIMESTAMP"))
            await conn.commit()

        print("\nSchema sync completed!")

if __name__ == "__main__":
    asyncio.run(sync_schema())