import pandas as pd
from backend.src.models.predict_model import PredictionModel

model = PredictionModel()

sample = pd.DataFrame(
    {
        "store":[1],
        "item":[1],
        "year":[2017],
        "month":[1],
        "day":[1],
        "daysofweek":[6],
        "weekofyear":[1],
        "quarter":[1],
        "is_weekend":[1],
        "lag_1":[15],
        "lag_7":[14],
        "lag_30":[16],
        "rolling_mean_7":[14.8],
        "rolling_std_7":[1.2345],
        "rolling_mean_30":[15.2],
        "rolling_std_30":[1.378],
    }
)

prediction = model.predict(sample)

print("prediction:",prediction)