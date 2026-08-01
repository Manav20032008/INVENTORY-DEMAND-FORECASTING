from src.preprocessing.data_loader import DataLoader
from src.preprocessing.data_validation import DataValidator

loader = DataLoader()
df = loader.load_csv("Inventory_Demand/data/raw/train.csv")

validator = DataValidator()
validator.check_empty_dataframe(df)
validator.check_missing_values(df)
validator.check_duplicates(df)

validator.validate_columns(df,["date","store","item","sales"])
print(df.head())