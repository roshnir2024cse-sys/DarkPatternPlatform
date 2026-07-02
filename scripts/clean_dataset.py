import pandas as pd

# Load dataset
df = pd.read_csv("../dataset/amazon.csv")

# -----------------------------
# Convert discounted_price
# -----------------------------
df["discounted_price"] = (
    df["discounted_price"]
    .str.replace("₹", "", regex=False)
    .str.replace(",", "", regex=False)
    .astype(float)
)

# -----------------------------
# Convert actual_price
# -----------------------------
df["actual_price"] = (
    df["actual_price"]
    .str.replace("₹", "", regex=False)
    .str.replace(",", "", regex=False)
    .astype(float)
)

# -----------------------------
# Convert discount_percentage
# -----------------------------
df["discount_percentage"] = (
    df["discount_percentage"]
    .str.replace("%", "", regex=False)
    .astype(float)
)

# -----------------------------
# Convert rating
# -----------------------------
df["rating"] = pd.to_numeric(df["rating"], errors="coerce")

# -----------------------------
# Convert rating_count
# -----------------------------
df["rating_count"] = (
    df["rating_count"]
    .fillna("0")
    .str.replace(",", "", regex=False)
)

df["rating_count"] = pd.to_numeric(df["rating_count"], errors="coerce")

# -----------------------------
# Save cleaned dataset
# -----------------------------
df.to_csv("../dataset/amazon_clean.csv", index=False)

print("✅ Dataset Cleaned Successfully!")

print("\nData Types:\n")
print(df.dtypes)