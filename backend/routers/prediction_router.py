from fastapi import APIRouter , Depends ,Query
from sqlalchemy.orm import Session
from typing import List
from backend.database.connection import get_db

from backend.schemas.prediction_schema import (
    PredictionRequest,
    PredictionResponse
)
from backend.schemas.history_schema import PredictionHistoryResponse
from backend.schemas.analytics_schema import AnalyticsResponse
from backend.services.prediction_service import PredictionServices


router = APIRouter()
prediction_services = PredictionServices()

@router.post("/predict",response_model = PredictionResponse)
def predict(request : PredictionRequest,
            db: Session = Depends(get_db)):
    prediction = prediction_services.predict(db=db,request_data=request.model_dump())

    return PredictionResponse(predicted_sales=prediction)




@router.get("/predictions",response_model = List[PredictionHistoryResponse])
def get_prediction(db: Session = Depends(get_db), page: int = Query(1, ge=1),
    limit: int = Query(20, ge=1, le=100),  store: int | None = Query(None)):
    return prediction_services.get_prediction_history(db=db , page = page , limit=limit , store = store )



@router.get("/analytics",response_model=AnalyticsResponse)
def analytics(db: Session = Depends(get_db)) :
    return prediction_services.get_dashboard_analytics(db)