from backend.database.connection import engine
from backend.database.base import Base
from backend.models.prediction_history import PredictionHistory  
from backend.models.user import User 

Base.metadata.create_all(bind=engine)
print("tables created successfuly")
