from fastapi import FastAPI
from pathlib import Path
from api.schemas import ProductInput
import joblib
import pandas as pd
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(
    title="Dark Pattern AI API",
    version="1.0"
)

    
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# -----------------------------
# Load ML Model
# -----------------------------
BASE_DIR = Path(__file__).resolve().parent.parent

model = joblib.load(BASE_DIR / "ML" / "model.pkl")
encoder = joblib.load(BASE_DIR / "ML" / "label_encoder.pkl")


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
    confidence = float(probability.max() * 100)

    return {
        "RiskLevel": risk,
        "Confidence": round(confidence, 2)
    }
