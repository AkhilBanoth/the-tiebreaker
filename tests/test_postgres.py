
import asyncio
from sqlalchemy import text

from app.db.postgres import engine


async def test_postgres_connection():
    try:
        async with engine.connect() as connection:
            result = await connection.execute(text("SELECT version()"))

            print("PostgreSQL connected successfully!")
            print("Database version:")
            print(result.scalar())

    except Exception as error:
        print("PostgreSQL connection failed:")
        print(error)

    finally:
        await engine.dispose()


if __name__ == "__main__":
    asyncio.run(test_postgres_connection())
