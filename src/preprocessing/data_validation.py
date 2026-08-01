import pandas as pd 

class DataValidator :

    @staticmethod
    def check_empty_dataframe(df: pd.DataFrame) :
        if df.empty:
            raise ValueError("DataFrame is Empty.")
        
    @staticmethod
    def check_missing_values(df: pd.DataFrame) :
        missing = df.isnull().sum()

        print(f"\nMissing Values...{missing}")
        return missing

    @staticmethod
    def check_duplicates(df: pd.DataFrame):
        duplicates = df.duplicated().sum()

        print(f"\nDuplicate Rows: {duplicates}")
        return duplicates

    @staticmethod
    def validate_columns(df: pd.DataFrame, required_columns:list) :
        missing_columns = [col for col in required_columns if col not in df.columns ]

        
        if missing_columns :
            raise ValueError(f"Missing Columns: {missing_columns}")
          