
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Central configuration for The Tiebreaker."""

    app_name: str = "The Tiebreaker"
    app_env: str = "development"
    debug: bool = True

    # Gemini
    gemini_api_key: str | None = None
    gemini_model: str = "gemini-2.5-flash"

    # PostgreSQL
    database_url: str = (
        "postgresql+asyncpg://postgres:password@localhost:5432/tiebreaker"
    )

    # MongoDB
    mongo_uri: str = "mongodb://localhost:27017"
    mongo_db_name: str = "tiebreaker"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )


settings = Settings()
