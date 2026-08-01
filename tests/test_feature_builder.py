from src.preprocessing.data_loader import DataLoader
from src.preprocessing.data_cleaning import DataCleaner
from src.feature_engineering.feature_builder import FeatureBuilder


loader = DataLoader()
df = loader.load_csv("Inventory_Demand/data/raw/train.csv")

df = DataCleaner.clean_data(df)
df = FeatureBuilder.build(df)

print(df.head())
print(df.columns)