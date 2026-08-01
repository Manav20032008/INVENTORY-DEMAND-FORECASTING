from backend.src.preprocessing.data_loader import DataLoader
from backend.src.preprocessing.data_cleaning import DataCleaner

loader = DataLoader()

df = loader.load_csv("Inventory_Demand/data/raw/train.csv")

clean_df = DataCleaner.clean_data(df)

print(clean_df.info())
print(clean_df.head())