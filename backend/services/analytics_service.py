from sqlalchemy.orm import Session

from backend.repositories.prediction_repository import PredictionRepository


class AnalyticsService:
    @staticmethod
    def get_dashboard_analytics(db: Session) -> dict:
        return PredictionRepository.get_analytics(db)
