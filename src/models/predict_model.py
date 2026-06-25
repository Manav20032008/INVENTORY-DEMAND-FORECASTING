import joblib
from backend.core.settings import settings

class PredictionModel:

    def __init__ (self):
        self.model = joblib.load(settings.MODEL_PATH)

        self.feature_columns = joblib.load(
            "artifacts/feature_columns.pkl")
        
    def predict(self, x):
        x = x[self.feature_columns]

        prediction = self.model.predict(x)

        return prediction