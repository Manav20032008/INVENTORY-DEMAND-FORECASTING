from backend.src.preprocessing.data_loader import DataLoader
from backend.src.preprocessing.data_cleaning import DataCleaner
from backend.src.feature_engineering.date_features import DateFeatures
from backend.src.feature_engineering.lag_features import LagFeatures

loader = DataLoader()

df = loader.load_csv(
    "Inventory_Demand/data/raw/train.csv"
)

df = DataCleaner.clean_data(df)
df = DateFeatures.feature(df)
df = LagFeatures.lag(df)


print(
    df[
        [
            "date",
            "sales",
            "lag_1",
            "lag_7",
            "lag_30"
        ]
    ].head(35)
)
