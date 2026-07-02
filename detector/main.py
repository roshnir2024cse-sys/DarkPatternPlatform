import pandas as pd

from fake_discount import detect_fake_discount
from review_trust import detect_review_risk
from pricing_risk import detect_pricing_risk
from scoring import calculate_score

# Load cleaned dataset
df = pd.read_csv("../dataset/amazon_features.csv")

# Run detectors
df = detect_fake_discount(df)
df = detect_review_risk(df)
df = detect_pricing_risk(df)
# Calculate score
df = calculate_score(df)

# Save output
df.to_csv("../dataset/final_output.csv", index=False)

print("✅ Dark Pattern Detection Completed!")

print(df[[
    "product_name",
    "PotentialFakeDiscount",
    "ReviewTrustRisk",
    "PremiumDiscountRisk",
    "DarkPatternScore",
    "RiskLevel"
]].head())