from pydantic import BaseModel

class PredictionRequest(BaseModel):
    store: int
    item: int
    year: int
    month: int
    day: int
    daysofweek: int
    weekofyear: int
    quarter: int
    is_weekend: int
    lag_1: float
    lag_7: float
    lag_30: float
    rolling_mean_7: float
    rolling_std_7: float
    rolling_mean_30: float
    rolling_std_30: float


class PredictionResponse(BaseModel):
    predicted_sales: float