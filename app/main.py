
from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.config import settings
from app.db.postgres import engine
from app.db.mongodb import check_mongodb, close_mongodb


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Manage database connections during application startup and shutdown."""

    # Startup
    print("Starting The Tiebreaker API...")

    try:
        # Check PostgreSQL
        async with engine.connect() as connection:
            print("PostgreSQL connected successfully!")

        # Check MongoDB
        await check_mongodb()
        print("MongoDB connected successfully!")

        yield

    finally:
        # Shutdown
        print("Closing database connections...")

        await engine.dispose()
        await close_mongodb()

        print("Database connections closed.")


app = FastAPI(
    title=settings.app_name,
    description=(
        "An AI-powered decision intelligence engine "
        "with dynamic scoring, sensitivity analysis, "
        "explainable recommendations and decision history."
    ),
    version="0.1.0",
    debug=settings.debug,
    lifespan=lifespan,
)


@app.get("/", tags=["General"])
async def root():
    return {
        "message": "Welcome to The Tiebreaker API!",
        "application": settings.app_name,
        "version": "0.1.0",
    }


@app.get("/health", tags=["General"])
async def health_check():
    return {
        "status": "healthy",
        "service": "the-tiebreaker-api",
        "databases": {
            "postgresql": "connected",
            "mongodb": "connected",
        },
    }
