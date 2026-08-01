from functools import lru_cache
from typing import List

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    APP_ENV: str = "development"
    API_HOST: str = "127.0.0.1"
    API_PORT: int = 8000
    API_TITLE: str = "Inventory Demand API"
    API_VERSION: str = "1.0.0"
    API_PREFIX: str = "/api/v1"

    MODEL_PATH: str = "artifacts/xgb_model.pkl"
    FEATURE_COLUMNS_PATH: str = "artifacts/feature_columns.pkl"

    DATABASE_URL: str = "postgresql://postgres:postgres@localhost:5432/inventory_demand"
    LOG_LEVEL: str = "INFO"

    CORS_ORIGINS: List[str] = [
        "http://localhost:5173",
        "http://127.0.0.1:5173",
        "http://localhost:3000",
    ]


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
