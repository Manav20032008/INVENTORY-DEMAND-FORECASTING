from src.feature_engineering.lag_features import LagFeatures
from src.feature_engineering.rolling_features import RollingFeatures
from src.feature_engineering.date_features import DateFeatures


class FeatureBuilder:
    @staticmethod
    def build(df):
        df = DateFeatures.feature(df)
        df = LagFeatures.lag(df)
        df = RollingFeatures.rolling(df)
        return df