import joblib

from backend.core.settings import settings
from backend.exceptions.custom_exceptions import ModelNotFoundException

class PredictionModel:
    def __init__(self):
        try:
            self.model = joblib.load(settings.MODEL_PATH)
            self.feature_columns = joblib.load(settings.FEATURE_COLUMNS_PATH)
        except FileNotFoundError as exc:
            raise ModelNotFoundException(str(exc)) from exc

    def predict(self, x):
        x = x[self.feature_columns]
        return self.model.predict(x)
