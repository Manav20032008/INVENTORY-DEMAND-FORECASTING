import joblib
from pathlib import Path
from src.pipelines.data_pipeline import DataPipeline
from src.models.train_xgboost import XGBoostTainer
from src.evaluation.metrics import RegressionMetrics

class TrainingPipeline:

    def __init__(self):

        self.data_pipeline = DataPipeline()
        self.model_trainer = XGBoostTainer()

    def run(self):
        print("Running Training Pipeline ...")

        df = self.data_pipeline.run()

        df = df.dropna()

        train_df = df[
            df['date'] < "2017-01-01"
        ]

        test_df = df[
            df['date'] >= "2017-01-01"
        ]

        features = [
            col 
            for col in df.columns
            if col not in ["date","sales"]
        ]

        x_train = train_df[features]
        y_train = train_df["sales"]

        x_test = test_df[features]
        y_test = test_df["sales"]

        model = (self.model_trainer.train(x_train,x_test))

        predictions = (model.predict(x_test))

        metrics = (RegressionMetrics.evaluate(y_test,predictions))

        print("---Results---")
        for key, value in metrics.items():
            print(f"{key}: {value:.4f}")

        artifacts_dir = Path("artifacts")

        artifacts_dir.mkdir(exist_ok=True)

        joblib.dump(model,artifacts_dir
            /"xgb_model.pkl"
        )

        print("Model Saved Successfully.")

        return model