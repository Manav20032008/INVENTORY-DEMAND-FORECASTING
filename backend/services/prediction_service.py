from pathlib import Path

import joblib
from sqlalchemy.orm import Session

from backend.core.settings import settings
from backend.exceptions.custom_exceptions import ModelNotFoundException, PredictionException
from backend.logging.logger import get_logger
from backend.repositories.prediction_repository import PredictionRepository
from src.pipeline.prediction_pipeline import PredictionPipeline

logger = get_logger()


class PredictionService:
    def __init__(self):
        self.pipeline = PredictionPipeline()
        self._validate_artifacts()

    def _validate_artifacts(self) -> None:
        model_path = Path(settings.MODEL_PATH)
        feature_path = Path(settings.FEATURE_COLUMNS_PATH)
        if not model_path.exists() or not feature_path.exists():
            raise ModelNotFoundException(
                f"Model artifacts not found at {model_path} or {feature_path}"
            )

    def predict(self, db: Session, request_data: dict) -> float:
        try:
            prediction = self.pipeline.predict(request_data)
            PredictionRepository.save_prediction(
                db=db,
                store=request_data["store"],
                item=request_data["item"],
                prediction=prediction,
            )
            logger.info(
                "prediction_saved store=%s item=%s prediction=%.4f",
                request_data["store"],
                request_data["item"],
                prediction,
            )
            return prediction
        except ModelNotFoundException:
            raise
        except Exception as exc:
            logger.exception("prediction_failed")
            raise PredictionException(str(exc)) from exc

    def get_prediction_history(
        self,
        db: Session,
        page: int,
        limit: int,
        store: int | None = None,
    ):
        return PredictionRepository.get_predictions(
            db=db,
            page=page,
            limit=limit,
            store=store,
        )


# Backward-compatible alias
PredictionServices = PredictionService
