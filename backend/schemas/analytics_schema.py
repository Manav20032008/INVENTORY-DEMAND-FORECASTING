from pydantic import BaseModel


class AnalyticsResponse(BaseModel):
    total_predictions: int
    average_prediction: float
    highest_prediction: float
    lowest_prediction: float