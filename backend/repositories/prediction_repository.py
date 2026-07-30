from backend.models.prediction_history import PredictionHistory
from sqlalchemy import func


class PredictionRepository:

    @staticmethod
    def save_prediction(db,store,item,prediction):
        prediction_record = (
            PredictionHistory(store=store,item=item,
                              prediction=prediction)
        )

        db.add(prediction_record)

        db.commit()

        db.refresh(prediction_record)

        return prediction_record
    


    @staticmethod
    def get_prediction(db , page: int = 1 , limit: int = 20 , store: int | None = None):
        query = db.query(PredictionHistory)

        if store is not None :
            query = query.filter( PredictionHistory.store == store)

        return query.order_by(PredictionHistory.created_at.desc()).offset((page-1)*limit).limit(limit).all()
    

    @staticmethod
    def get_analytics(db) :
        total = db.query(PredictionHistory).count()
        avg = db.query(func.avg(PredictionHistory.prediction).scalar() or 0)
        highest = db.query(func.max(PredictionHistory.prediction).scalar() or 0)
        lowest = db.query(func.min(PredictionHistory.prediction).scalar() or 0)

        return {"total_predictions": total,"average_prediction": avg,
        "highest_prediction": highest,"lowest_prediction": lowest}
    