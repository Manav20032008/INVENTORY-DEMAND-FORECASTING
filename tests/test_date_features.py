from src.preprocessing.data_loader import DataLoader
from src.preprocessing.data_cleaning import DataCleaner
from src.feature_engineering.date_features import DateFeatures


loader = DataLoader()

df = loader.load_csv(
    "Inventory_Demand/data/raw/train.csv"
)

df = DataCleaner.clean_data(df)

df = DateFeatures.feature(df)

print(df.head())
print(df.columns)