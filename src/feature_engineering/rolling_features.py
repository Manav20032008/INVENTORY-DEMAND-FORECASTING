import pandas as pd

class RollingFeatures :

    @staticmethod
    def rolling_mean_7(df : pd.DataFrame) -> pd.DataFrame :

        df["rolling_mean_7"] = (
            df.groupby(['store' , 'item'])["sales"].transform(
                lambda x : x.shift(1).rolling(7).mean()
            )
        )

        return df
    
    @staticmethod
    def rolling_mean_30(df : pd.DataFrame) -> pd.DataFrame :

        df["rolling_mean_30"] = (
            df.groupby(['store' , 'item'])["sales"].transform(
                lambda x : x.shift(1).rolling(30).mean()
            )
        )

        return df
    
    @staticmethod
    def rolling_std_7(df : pd.DataFrame) -> pd.DataFrame :

        df["rolling_std_7"] = (
            df.groupby(['store' , 'item'])["sales"].transform(
                lambda x : x.shift(1).rolling(7).std()
            )
        )

        return df
    
    @staticmethod
    def rolling_std_30(df : pd.DataFrame) -> pd.DataFrame :

        df["rolling_std_30"] = (
            df.groupby(['store' , 'item'])["sales"].transform(
                lambda x : x.shift(1).rolling(30).std()
            )
        )

        return df
    
    @staticmethod
    def rolling(df : pd.DataFrame) -> pd.DataFrame :

        df = RollingFeatures.rolling_mean_7(df)
        df = RollingFeatures.rolling_mean_30(df)
        df = RollingFeatures.rolling_std_7(df)
        df = RollingFeatures.rolling_std_30(df)

        return df 