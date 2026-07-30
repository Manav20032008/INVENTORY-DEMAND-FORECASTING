from src.pipeline.prediction_pipeline import PredictionPipeline
from backend.repositories.prediction_repository import PredictionRepository


class PredictionServices :

    def __init__(self):

        self.pipeline = PredictionPipeline()

    def predict(self, db,  request_data: dict):
        prediction = self.pipeline.predict(request_data)

        PredictionRepository.save_prediction(db=db,
                        store=request_data["store"],
                        item=request_data["item"],
                        prediction=prediction      )

        return prediction
        
    def get_prediction_history(self,db , page: int, limit: int, store: int| None = None ) :

        return PredictionRepository.get_prediction(db=db , page=page ,limit=limit, store=store )
    
    def get_dashboard_analytics(self,db):
        return PredictionRepository.get_analytics(db)