from backend.models.prediction_history import PredictionHistory
from sqlalchemy import func
from sqlalchemy.orm import Session
 

class PredictionRepository:
    @staticmethod
    def save_prediction(db: Session, store: int, item: int, prediction: float):
        prediction_record = PredictionHistory(store=store,item=item,
                                              prediction=prediction,)
        
        db.add(prediction_record)
        db.commit()
        db.refresh(prediction_record)

        return prediction_record



    @staticmethod
    def get_predictions(db: Session,page: int = 1,limit: int = 20,store: int | None = None,):
        query = db.query(PredictionHistory)

        if store is not None:
            query = query.filter(PredictionHistory.store == store)

        return (query.order_by(PredictionHistory.created_at.desc()).offset((page - 1) * limit).limit(limit).all())



    @staticmethod
    def get_analytics(db: Session) -> dict:
        total = db.query(PredictionHistory).count()
        avg = db.query(func.avg(PredictionHistory.prediction)).scalar() or 0.0
        highest = db.query(func.max(PredictionHistory.prediction)).scalar() or 0.0
        lowest = db.query(func.min(PredictionHistory.prediction)).scalar() or 0.0


        unique_stores = db.query(func.count(func.distinct(PredictionHistory.store))).scalar() or 0
        unique_items = db.query(func.count(func.distinct(PredictionHistory.item))).scalar() or 0

        return {"total_predictions": total,"average_prediction": float(avg),"highest_prediction": float(highest),
                "lowest_prediction": float(lowest),"unique_stores": int(unique_stores),"unique_items": int(unique_items),}
