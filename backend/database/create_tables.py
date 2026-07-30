from backend.database.connection import engine
from backend.database.base import Base
from backend.models.user import User
from backend.models.prediction_history import PredictionHistory

Base.metadata.create_all(bind=engine)
print("Tables created Successfully.")