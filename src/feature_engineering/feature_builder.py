from backend.src.feature_engineering.lag_features import LagFeatures
from backend.src.feature_engineering.rolling_features import RollingFeatures
from backend.src.feature_engineering.date_features import DateFeatures


class FeatureBuilder:

    @staticmethod
    def build(df):

        print("Creating Date Features...")
        df = DateFeatures.feature(df)

        print("Creating Lag Features...")
        df = LagFeatures.lag(df)

        print("Creating Rolling Features...")
        df = RollingFeatures.rolling(df)

        return df