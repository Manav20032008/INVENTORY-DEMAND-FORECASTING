import joblib

class PredictionModel:

    def __init__ (self):
        self.model = joblib.load("artifacts/xgb_model.pkl")

        self.feature_columns = joblib.load(
            "artifacts/feature_columns.pkl")
        
    def predict(self, x):
        x = x[self.feature_columns]

        prediction = self.model.predict(x)

        return prediction