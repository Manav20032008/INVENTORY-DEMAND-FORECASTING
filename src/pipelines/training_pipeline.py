import joblib
import json
from pathlib import Path
from src.pipelines.data_pipeline import DataPipeline
from src.models.train_xgboost import XGBoostTainer
from src.evaluation.metrics import RegressionMetrics

class TrainingPipeline:

    def __init__(self):

        self.data_pipeline = DataPipeline()
        self.model_trainer = XGBoostTainer()

    def feature_model(self,features):
        joblib.dump(features,"artifacts/feature_columns.pkl")

    def metrics_model(self,metrics):
        with open("artifacts/metrics.json","w") as f :
            json.dump(metrics,f,indent=4)

    def metadata_model(self,features):
        metadata = {
            "model_name":"XGBoost",
            "version":"1.0",
            "feature_count":len(features)
        }

        with open("artifacts/model_metadata.json","w") as f:
            json.dump(metadata,f,indent=4)


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

        model = (self.model_trainer.train(x_train,y_train))

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

        self.feature_model(features)
        self.metrics_model(metrics)
        self.metadata_model(features)


        print("Model Saved Successfully.")

        return model