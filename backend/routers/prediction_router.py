from fastapi import APIRouter

from backend.schemas.prediction_schema import (
    PredictionRequest,
    PredictionResponse
)
from backend.services.prediction_service import PredictionService


router = APIRouter()
prediction_services = PredictionService()

@router.post(
    "/predict",
    response_model = PredictionResponse
)
def predict(request : PredictionRequest):
    prediction = prediction_services.predict(request.model_dump())

    return PredictionResponse(predicted_sales=prediction)