
import asyncio

from app.db.mongodb import mongo_client, mongo_database


async def test_mongodb_connection():
    try:
        result = await mongo_database.command("ping")

        if result.get("ok") == 1:
            print("MongoDB connected successfully!")
            print("Database name:", mongo_database.name)

    except Exception as error:
        print("MongoDB connection failed:")
        print(error)

    finally:
        await mongo_client.close()


if __name__ == "__main__":
    asyncio.run(test_mongodb_connection())
