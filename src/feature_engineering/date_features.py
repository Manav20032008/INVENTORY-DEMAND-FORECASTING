import pandas as pd

class DateFeatures :

    @staticmethod
    def create_year(df : pd.DataFrame) -> pd.DataFrame :
        df["year"] = df["date"].dt.year 
        return df 
    
    @staticmethod
    def create_month(df: pd.DataFrame) -> pd.DataFrame :
        df["month"] =df["date"].dt.month
        return df
    
    @staticmethod
    def create_day(df : pd.DataFrame) -> pd.DataFrame :
        df["day"] = df["date"].dt.year
        return df
    
    @staticmethod
    def create_daysofweek(df: pd.DataFrame) -> pd.DataFrame :
        df["daysofweek"] = df["date"].dt.dayofweek
        return df
    
    @staticmethod
    def create_weekofyear(df : pd.DataFrame) -> pd.DataFrame :
        df["weekofyear"] = (
            df["date"].dt.isocalendar().week.astype(int)
            )
        return df
    
    @staticmethod
    def create_quarter(df : pd.DataFrame) -> pd.DataFrame :
        df["quarter"] = df["date"].dt.quarter
        return df
    
    @staticmethod
    def create_weekend_flag(df : pd.DataFrame) -> pd.DataFrame :
        df["is_weekend"] = (
            df["daysofweek"] >= 5
        ).astype(int)

        return df

    @staticmethod
    def feature(df: pd.DataFrame) -> pd.DataFrame:
        df = DateFeatures.create_year(df)
        df = DateFeatures.create_month(df)
        df = DateFeatures.create_day(df)
        df = DateFeatures.create_daysofweek(df)
        df = DateFeatures.create_weekofyear(df)
        df = DateFeatures.create_quarter(df)
        df = DateFeatures.create_weekend_flag(df)

        return df
