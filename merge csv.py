import pandas as pd
import glob
import os

# Point this to your extracted folder path
folder_path = r"C:\Users\Manoj\Downloads\files (1)"  

# Get all CSV files
all_files = glob.glob(os.path.join(folder_path, "*.csv"))

dfs = []
for file in all_files:
    df = pd.read_csv(file)
    df['category'] = os.path.basename(file).replace('.csv', '')  # add category column
    dfs.append(df)

# Merge all into one DataFrame
combined = pd.concat(dfs, ignore_index=True)
combined.to_csv('Combined_dataset.csv', index=False)

print(f"✅ Merged {len(all_files)} files → {combined.shape[0]:,} rows × {combined.shape[1]} columns")
print(combined.head())