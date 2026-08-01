from pathlib import Path

from sqlalchemy import text
from sqlalchemy.orm import Session

from backend.core.settings import settings
from backend.database.connection import engine



class HealthService:
    @staticmethod
    def check_database() -> str:
        try:
            with engine.connect() as connection:
                connection.execute(text("SELECT 1"))
            return "connected"
        except Exception:
            return "disconnected"

    @staticmethod
    def check_model() -> str:
        model_path = Path(settings.MODEL_PATH)
        feature_path = Path(settings.FEATURE_COLUMNS_PATH)

        if model_path.exists() and feature_path.exists():
            return "loaded"
        
        return "missing"

    @staticmethod
    def get_health(db: Session | None = None) -> dict:
        db_status = HealthService.check_database()
        model_status = HealthService.check_model()

        overall = "healthy" if db_status == "connected" and model_status == "loaded" else "degraded"


        return {"status": overall,"database": db_status,"model": model_status,"version": settings.API_VERSION,}
