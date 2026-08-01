from backend.database.connection import engine
from backend.database.base import Base
from backend.models.prediction_history import PredictionHistory  # noqa: F401
from backend.models.user import User  # noqa: F401

Base.metadata.create_all(bind=engine)
print("Tables created successfully.")
