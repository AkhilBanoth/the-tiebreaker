
from pymongo import AsyncMongoClient
from pymongo.asynchronous.database import AsyncDatabase

from app.config import settings


mongo_client = AsyncMongoClient(
    settings.mongo_uri,
    serverSelectionTimeoutMS=5000,
)

mongo_database: AsyncDatabase = mongo_client[settings.mongo_db_name]


async def check_mongodb() -> bool:
    await mongo_database.command("ping")
    return True


async def close_mongodb() -> None:
    await mongo_client.close()
