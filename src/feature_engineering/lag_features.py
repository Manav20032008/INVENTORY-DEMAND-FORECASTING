import pandas as pd 

class LagFeatures:

    @staticmethod
    def create_lag_1(df: pd.DataFrame) ->pd.DataFrame :
        df["lag_1"] = (df.groupby(["store","item"])["sales"].shift(1))
        return df
    
    @staticmethod
    def create_lag_7(df: pd.DataFrame) -> pd.DataFrame :
        df["lag_7"] = (df.groupby(["store","item"])["sales"].shift(7))
        return df
    
    @staticmethod
    def create_lag_30(df: pd.DataFrame)-> pd.DataFrame:
        df["lag_30"] = (df.groupby(["store","item"])["sales"].shift(30))
        return df
    
    @staticmethod
    def lag(df : pd.DataFrame) -> pd.DataFrame :
        df = LagFeatures.create_lag_1(df)
        df = LagFeatures.create_lag_7(df)
        df = LagFeatures.create_lag_30(df)
        return df