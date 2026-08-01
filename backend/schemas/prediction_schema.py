from pydantic import BaseModel, Field


class PredictionRequest(BaseModel):
    store: int = Field(..., ge=1)
    item: int = Field(..., ge=1)
    year: int = Field(..., ge=2013, le=2030)
    month: int = Field(..., ge=1, le=12)
    day: int = Field(..., ge=1, le=31)
    daysofweek: int = Field(..., ge=0, le=6)
    weekofyear: int = Field(..., ge=1, le=53)
    quarter: int = Field(..., ge=1, le=4)
    is_weekend: int = Field(..., ge=0, le=1)
    lag_1: float
    lag_7: float
    lag_30: float
    rolling_mean_7: float
    rolling_std_7: float
    rolling_mean_30: float
    rolling_std_30: float


class PredictionResponse(BaseModel):
    predicted_sales: float
    store: int
    item: int
