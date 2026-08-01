from src.preprocessing.data_loader import DataLoader
from src.preprocessing.data_cleaning import DataCleaner
from src.feature_engineering.feature_builder import FeatureBuilder

class DataPipeline:
    def __init__(self):
        self.loader = DataLoader()

    def run(self,file_path: str = "data/raw/train.csv"):
        df = self.loader.load_csv(file_path)
        df = DataCleaner.clean_data(df)
        df = FeatureBuilder.build(df)
        return df