from pydantic import BaseModel
from datetime import datetime

class PredictionHistoryResponse(BaseModel):
    id:int
    store:int
    item:int
    prediction:float
    created_at:datetime

    class Config:
        from_attributes = True