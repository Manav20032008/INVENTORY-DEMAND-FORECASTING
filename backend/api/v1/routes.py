from typing import List
from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from backend.core.dependencies import (get_analytics_service,get_db,get_prediction_service,)
from backend.schemas.analytics_schema import AnalyticsResponse
from backend.schemas.health_schema import HealthResponse
from backend.schemas.history_schema import PredictionHistoryResponse
from backend.schemas.prediction_schema import PredictionRequest, PredictionResponse
from backend.services.analytics_service import AnalyticsService
from backend.services.health_service import HealthService
from backend.services.prediction_service import PredictionService

router = APIRouter()


@router.get("/health", response_model=HealthResponse, tags=["Health"])
def health_check(db: Session = Depends(get_db)):
    return HealthService.get_health(db)


@router.post("/predict", response_model=PredictionResponse, tags=["Predictions"])
def predict(request: PredictionRequest,db: Session = Depends(get_db),prediction_service: PredictionService = Depends(get_prediction_service),):
    prediction = prediction_service.predict(db=db, request_data=request.model_dump())
    return PredictionResponse(predicted_sales=prediction,store=request.store,item=request.item,)


@router.get("/predictions",response_model=List[PredictionHistoryResponse],tags=["Predictions"],)
def get_predictions(db: Session = Depends(get_db),page: int = Query(1, ge=1),limit: int = Query(20, ge=1, le=100),store: int | None = Query(None),prediction_service: PredictionService = Depends(get_prediction_service),):
    return prediction_service.get_prediction_history(db=db,page=page,limit=limit,store=store,)


@router.get("/analytics", response_model=AnalyticsResponse, tags=["Analytics"])
def analytics(db: Session = Depends(get_db),analytics_service: AnalyticsService = Depends(get_analytics_service),):
    return analytics_service.get_dashboard_analytics(db)
