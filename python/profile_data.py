from pathlib import Path
import pandas as pd

raw_folder = Path("data/raw")

print(raw_folder.resolve())
print(raw_folder.exists())

for csv_file in raw_folder.glob("*.csv"):
    print("=" * 70)
    print(f"FILE: {csv_file.name}")

    df = pd.read_csv(csv_file)

    print(f"Rows: {len(df):,}")
    print(f"Columns: {len(df.columns)}")

    print("\nColumns:")
    print(df.dtypes)

    print("\nMissing Values:")
    print(df.isnull().sum())

    print("\nDuplicate Rows:")
    print(df.duplicated().sum())

    print("\nFirst 5 Rows:")
    print(df.head())

    print()