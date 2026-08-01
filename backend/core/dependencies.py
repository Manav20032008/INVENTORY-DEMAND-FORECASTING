from functools import lru_cache
from collections.abc import Generator

from sqlalchemy.orm import Session

from backend.core.settings import settings
from backend.database.connection import SessionLocal
from backend.services.analytics_service import AnalyticsService
from backend.services.prediction_service import PredictionService


def get_db() -> Generator[Session, None, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@lru_cache
def get_prediction_service() -> PredictionService:
    return PredictionService()


def get_analytics_service() -> AnalyticsService:
    return AnalyticsService()


def get_settings_dep():
    return settings
