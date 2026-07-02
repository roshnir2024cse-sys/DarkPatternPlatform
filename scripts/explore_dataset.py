import pandas as pd

# Load the dataset
df = pd.read_csv("../dataset/amazon.csv")

print("=" * 50)
print("DATASET INFORMATION")
print("=" * 50)

print("\nShape of Dataset:")
print(df.shape)

print("\nColumn Names:")
print(df.columns.tolist())

print("\nFirst 5 Rows:")
print(df.head())

print("\nMissing Values:")
print(df.isnull().sum())

print("\nData Types:")
print(df.dtypes)