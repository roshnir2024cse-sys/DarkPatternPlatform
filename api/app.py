from fastapi import FastAPI
from schemas import ProductInput
import joblib
import pandas as pd

app = FastAPI(
    title="Dark Pattern AI API",
    version="1.0"
)

# Load model
model = joblib.load("../ML/model.pkl")
encoder = joblib.load("../ML/label_encoder.pkl")


@app.get("/")
def home():
    return {
        "message": "Dark Pattern AI API is Running!"
    }


@app.post("/predict")
def predict(product: ProductInput):

    data = pd.DataFrame([{
        "discount_percentage": product.discount_percentage,
        "rating": product.rating,
        "rating_count": product.rating_count,
        "actual_price": product.actual_price,
        "discounted_price": product.discounted_price
    }])

    prediction = model.predict(data)
    probability = model.predict_proba(data)

    risk = encoder.inverse_transform(prediction)[0]

    return {
        "RiskLevel": risk,
        "Confidence": round(probability.max() * 100, 2)
    }
