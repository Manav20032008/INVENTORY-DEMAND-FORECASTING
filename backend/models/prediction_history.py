from sqlalchemy import (Column,Integer,Float,DateTime)
from datetime import datetime
from backend.database.base import Base


class PredictionHistory(Base):

    __tablename__ = ("prediction_history")

    id = Column(Integer,primary_key=True,index=True)
    store = Column(Integer)
    item = Column(Integer)
    prediction = Column(Float)

    created_at = Column(DateTime,default=datetime.utcnow)