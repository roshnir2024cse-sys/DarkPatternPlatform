import pandas as pd
import numpy as np

# Load cleaned dataset
df = pd.read_csv("../dataset/amazon_clean.csv")
# Extract only the main category
df["MainCategory"] = df["category"].str.split("|").str[0]

# -----------------------------
# Rule 1: High Discount
# -----------------------------
df["HighDiscount"] = np.where(df["discount_percentage"] >= 70, "Yes", "No")

# -----------------------------
# Rule 2: Low Rating
# -----------------------------
df["LowRating"] = np.where(df["rating"] < 3.5, "Yes", "No")

# -----------------------------
# Rule 3: Low Reviews
# -----------------------------
df["LowReviewCount"] = np.where(df["rating_count"] < 100, "Yes", "No")

# -----------------------------
# Rule 4: Premium Product
# -----------------------------
df["PremiumProduct"] = np.where(df["actual_price"] > 10000, "Yes", "No")

# -----------------------------
# Rule 5: Very Large Description
# -----------------------------
df["LongDescription"] = np.where(
    df["about_product"].str.len() > 1000,
    "Yes",
    "No"
)

# Save
df.to_csv("../dataset/amazon_features.csv", index=False)

print("✅ Feature Engineering Completed")