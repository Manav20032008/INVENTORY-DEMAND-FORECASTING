import pandas as pd

class DataCleaner :

    @staticmethod 
    def convert_date(df: pd.DataFrame) -> pd.DataFrame :
        df["date"] = pd.to_datetime(df["date"])
        return df
    
    @staticmethod
    def sort_data(df: pd.DataFrame) -> pd.DataFrame :
        df = df.sort_values(
            by = ["store" , "item" , "date"]
        ).reset_index(drop = True)

        return df
    
    @staticmethod
    def remove_duplicates(df: pd.DataFrame) -> pd.DataFrame :
        before = len(df)

        df = df.drop_duplicates()

        after = len(df)

        print(f"Removed {before - after} Duplicates Rows.")

        return df
    
    @staticmethod
    def fill_missing_values(df: pd.DataFrame) -> pd.DataFrame :

        numeric_cols = df.select_dtypes(
            include = ["number"]
        ).columns

        for col in numeric_cols :
            df[col] = df[col].fillna(
                df[col].median()
            )
        
        return df
    
    @staticmethod
    def clean_data(df : pd.DataFrame) -> pd.DataFrame :

        df = DataCleaner.convert_date(df)
        df = DataCleaner.remove_duplicates(df)
        df = DataCleaner.fill_missing_values(df)
        df = DataCleaner.sort_data(df)

        return df
    