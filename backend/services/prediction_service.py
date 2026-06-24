from src.pipeline.prediction_pipeline import PredictionPipeline
from backend.logging.logger import get_logger

logger = get_logger()


class PredictionServices :

    def __init__(self):

        self.pipeline = PredictionPipeline()

        def predict(self, request_data: dict):

            logger.info("Prediction request received")

            prediction = self.pipeline.predict(request_data)

            logger.info(f"Prediction: {prediction}")
            
            return prediction
