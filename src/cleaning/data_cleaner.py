import yaml
import pandas as pd
from sklearn.preprocessing import OneHotEncoder, LabelEncoder, StandardScaler, MinMaxScaler

class DataCleaner:
    def __init__(self, path):
        if not path:
            raise ValueError("Invalid file path")
        
        if not path.endswith(".csv"):
            raise ValueError("File must be csv")
        
        self.df = pd.read_csv(path)
        self.rules = self.load_rules()


    def load_rules(self):
        with open("config/settings.yaml", "r") as f:
            return yaml.safe_load(f)

    def drop_columns(self):
        cols = self.rules.get("drop_columns",[])

        if cols:
            self.df.drop(columns=cols, inplace=True, errors="ignore")

    def handle_missing_values(self):
        missing_cfg = self.rules.get("missing_values",{})

        if not missing_cfg:
            return 
        for col, method in missing_cfg["strategy"].items():
            if method == "median":
                self.df[col] = self.df[col].fillna(self.df[col].median())
            elif method == "mode":
                self.df[col] = self.df[col].fillna(self.df[col].mode()[0])

    def encode_columns(self):
        encode = self.rules.get("encoding",{})
        if not encode:
            return 
        
        for col, method in self.rules["encoding"]["strategy"].items():
            if method == "label":
                le = LabelEncoder()
                self.df[col] = le.fit_transform(self.df[col].astype(str))
            elif method == "onehot":
                encoded = pd.get_dummies(self.df[col],prefix=col)
                self.df = pd.concat([self.df.drop(columns=[col]), encoded], axis=1)

    def scale_columns(self):
        scaling_cfg = self.rules.get("scaling",{})
        if not scaling_cfg:
            return
        for col, method in scaling_cfg["strategy"].items():
            if method == "standard":
                scaler = StandardScaler()
                self.df[col] = scaler.fit_transform(self.df[[col]])
            elif method == "minmax":
                scaler = MinMaxScaler()
                self.df[col] = scaler.fit_transform(self.df[[col]])

        

    def run_pipeline(self):
        self.drop_columns()
        self.handle_missing_values()
        self.encode_columns()
        self.scale_columns()
        return self.df
    
if __name__ == "__main__":
    cleaner = DataCleaner("data/raw/titanic.csv")
    clean_df = cleaner.run_pipeline()
    clean_df.to_csv("data/processed/cleaned titanic.csv", index=False)





