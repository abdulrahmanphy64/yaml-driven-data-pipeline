import os
import sys
from pathlib import Path
import pandas as pd
import numpy as np

class ExploreDataset:
    def __init__(self):
        os.makedirs("artifacts",exist_ok=True)
        self.path = os.path.join("artifacts","explore_dataset.txt")
        self.df = pd.read_csv("data/raw/titanic.csv")
        self.column_name = list(self.df.columns)


    def dataset_metadata(self):
        rows, col = self.df.shape
        data = {
            "Rows" : rows,
            "Columns" : col
        }
        return data

    def column_summary(self):
        columns = {}
        for column in self.column_name:
            columns[column] = {
                "Name" : column,
                "Type" : self.df[column].dtype,
                "Missing" : sum(self.df[column].isnull()),
                "Unique" : len(self.df[column].unique())
                }
        
        return columns
        

    def numerical_summary(self):
        numericals = {}
        for numerical in self.column_name:
            if self.df[numerical].dtype in ('int64','float64'):
                numericals[numerical] = {
                    "Name" : numerical,
                    "min" : min(self.df[numerical]),
                    "max" : max(self.df[numerical]),
                    "mean" : np.mean(self.df[numerical]),
                    "std" : np.std(self.df[numerical])
                }
            
        return numericals


    def categorical_summary(self):
        categories = {}
        for category in self.column_name:
            if self.df[category].dtype in ('object','O'):
                categories[category] = {
                    "Name" : category,
                    "Unique" : len(self.df[category].unique()),
                    "Top values" : self.df[category].unique()
                }
        return categories
    
    def sample_rows(self):
        return self.df.head()
    
    def generate_report(self):
        metadata = self.dataset_metadata()
        column_summary = self.column_summary()
        numerical_summary = self.numerical_summary()
        categorical_summary = self.categorical_summary()

        with open(self.path, "w", encoding="utf-8") as f:

            # ==== BASIC INFO ====
            f.write("==== DATASET METADATA ====\n")
            f.write(f"Rows: {metadata['Rows']}\n")
            f.write(f"Columns: {metadata['Columns']}\n\n")

            # ==== COLUMN SUMMARY ====
            f.write("==== COLUMN SUMMARY ====\n")
            for col, details in column_summary.items():
                f.write(f"\nColumn: {col}\n")
                f.write(f"  Type: {details['Type']}\n")
                f.write(f"  Missing: {details['Missing']}\n")
                f.write(f"  Unique Values: {details['Unique']}\n")
            f.write("\n")

            # ==== NUMERICAL SUMMARY ====
            f.write("==== NUMERICAL SUMMARY ====\n")
            for col, stats in numerical_summary.items():
                f.write(f"\nColumn: {col}\n")
                f.write(f"  Min: {stats['min']}\n")
                f.write(f"  Max: {stats['max']}\n")
                f.write(f"  Mean: {stats['mean']:.2f}\n")
                f.write(f"  Std Dev: {stats['std']:.2f}\n")
            f.write("\n")

            # ==== CATEGORICAL SUMMARY ====
            f.write("==== CATEGORICAL SUMMARY ====\n")
            for col, stats in categorical_summary.items():
                f.write(f"\nColumn: {col}\n")
                f.write(f"  Unique Values: {stats['Unique']}\n")

                # top 3 most frequent values
                top_values = self.df[col].value_counts().head(3)
                f.write("  Top Values:\n")
                for val, count in top_values.items():
                    f.write(f"    {val}: {count}\n")
            f.write("\n")

            # ==== SAMPLE ROWS ====
            f.write("==== SAMPLE ROWS (HEAD) ====\n")
            f.write(self.df.head().to_string())
            f.write("\n")

    
    


if __name__ == "__main__":
    Explore = ExploreDataset()
    Explore.generate_report()
