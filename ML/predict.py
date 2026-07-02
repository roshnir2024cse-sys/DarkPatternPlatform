import joblib
import pandas as pd

# Load model
model = joblib.load("model.pkl")
encoder = joblib.load("label_encoder.pkl")

print("===== Dark Pattern Risk Predictor =====")

discount = float(input("Discount Percentage: "))
rating = float(input("Rating: "))
rating_count = float(input("Rating Count: "))
actual_price = float(input("Actual Price: "))
discounted_price = float(input("Discounted Price: "))

data = pd.DataFrame([{
    "discount_percentage": discount,
    "rating": rating,
    "rating_count": rating_count,
    "actual_price": actual_price,
    "discounted_price": discounted_price
}])

prediction = model.predict(data)
probability = model.predict_proba(data)

risk = encoder.inverse_transform(prediction)[0]
confidence = probability.max() * 100

print("\n==============================")
print("Predicted Risk Level :", risk)
print(f"Confidence           : {confidence:.2f}%")
print("==============================")