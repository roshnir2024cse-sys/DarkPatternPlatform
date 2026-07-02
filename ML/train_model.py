import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, classification_report

# Load dataset
df = pd.read_csv("../dataset/final_output.csv")

# -----------------------------
# Data Cleaning
# -----------------------------

# Remove commas from numbers
df["actual_price"] = (
    df["actual_price"]
    .astype(str)
    .str.replace(",", "", regex=False)
    .astype(float)
)

df["discounted_price"] = (
    df["discounted_price"]
    .astype(str)
    .str.replace(",", "", regex=False)
    .astype(float)
)

df["rating"] = df["rating"].astype(float)

df["rating_count"] = (
    df["rating_count"]
    .fillna(0)
    .astype(str)
    .str.replace(",", "", regex=False)
    .astype(float)
)

df["discount_percentage"] = (
    df["discount_percentage"]
    .astype(str)
    .str.replace("%", "", regex=False)
    .astype(float)
)

# -----------------------------
# Features
# -----------------------------

X = df[
    [
        "discount_percentage",
        "rating",
        "rating_count",
        "actual_price",
        "discounted_price",
    ]
]

# Target
y = df["RiskLevel"]

# Encode labels
encoder = LabelEncoder()
y = encoder.fit_transform(y)

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Train Model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

# Prediction
y_pred = model.predict(X_test)

# Accuracy
print("\nAccuracy:", accuracy_score(y_test, y_pred))

print("\nClassification Report\n")
print(classification_report(y_test, y_pred))

# Save model
joblib.dump(model, "model.pkl")
joblib.dump(encoder, "label_encoder.pkl")

print("\n✅ Model Saved Successfully!")