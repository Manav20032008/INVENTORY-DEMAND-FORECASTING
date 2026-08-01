import pandas as pd
from src.models.predict_model import PredictionModel

class PredictionPipeline:

    def __init__(self):
        self.model = PredictionModel()

    def predict(self, data: dict):
        df = pd.DataFrame([data])
        prediction = self.model.predict(df)
        return float(prediction[0])