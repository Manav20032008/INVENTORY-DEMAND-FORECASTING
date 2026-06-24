from src.preprocessing.data_loader import DataLoader
from src.preprocessing.data_cleaning import DataCleaner
from src.feature_engineering.date_features import DateFeatures
from src.feature_engineering.lag_features import LagFeatures
from src.feature_engineering.rolling_features import RollingFeatures

loader = DataLoader()

df = loader.load_csv(
    "Inventory_Demand/data/raw/train.csv"
)

df = DataCleaner.clean_data(df)
df = DateFeatures.feature(df)
df = LagFeatures.lag(df)
df = RollingFeatures.rolling(df)

print(
    df[
        [
            "sales",
            "rolling_mean_7",
            "rolling_mean_30",
            "rolling_std_7",
            "rolling_std_30"
        ]
    ].head(50)
)