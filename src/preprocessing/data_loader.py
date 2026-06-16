from pathlib import Path
import pandas as pd

class DataLoader :

    def __init__(self):
        self.project_root = Path(__file__).resolve().parents[2]
    
    def load_csv(self, file_path: str) -> pd.dataFrame :

        full_path = self.project_root / file_path

        if not full_path.exists():
            raise FileNotFoundError(
                f"File not Found : {full_path} "
            )
        
        df = pd.read_csv(full_path)

        return df
    
    def save_csv(self, df:pd.dataFrame, file_path: str):

        full_path = self.project_root / file_path

        full_path.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        df.to_csv(full_path, index = False)

        print(f"Saved Succesfully : {full_path}")