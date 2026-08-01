from pathlib import Path
import pandas as pd

class DataLoader :

    def __init__(self):
        self.project_root = Path(__file__).resolve().parents[3]
    
    def load_csv(self, file_path: str) -> pd.DataFrame:
        full_path = self.project_root / file_path

        if not full_path.exists():
            raise FileNotFoundError(f"File not Found : {full_path} ")
        
        df = pd.read_csv(full_path)
        return df
    
    def save_csv(self, df:pd.DataFrame, file_path: str):
        full_path = self.project_root / file_path
        full_path.parent.mkdir(parents=True,exist_ok=True)

        df.to_csv(full_path, index = False)