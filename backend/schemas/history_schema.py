from pydantic import ConfigDict
from datetime import datetime

from pydantic import BaseModel


class PredictionHistoryResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    store: int
    item: int
    prediction: float
    created_at: datetime
