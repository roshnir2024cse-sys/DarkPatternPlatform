from fastapi import FastAPI
from pathlib import Path
from api.schemas import ProductInput
import joblib
import pandas as pd
from fastapi.middleware.cors import CORSMiddleware
import sqlite3
from database.db import SessionLocal
from database.models import Prediction
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
DB_PATH = BASE_DIR / "database" / "darkpattern.db"

model = joblib.load(BASE_DIR / "ML" / "model.pkl")
conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS predictions(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    discount_percentage REAL,
    rating REAL,
    rating_count REAL,
    actual_price REAL,
    discounted_price REAL,
    risk_level TEXT,
    confidence REAL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")

conn.commit()
conn.close()
encoder = joblib.load(BASE_DIR / "ML" / "label_encoder.pkl")


@app.get("/")
def home():
    return {
        "message": "Dark Pattern AI API is Running!"
    }


@app.post("/predict")
def predict(product: ProductInput):
    print("Prediction API Called")

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

    # Save to PostgreSQL
    db = SessionLocal()

    new_prediction = Prediction(
        discount_percentage=product.discount_percentage,
        rating=product.rating,
        rating_count=product.rating_count,
        actual_price=product.actual_price,
        discounted_price=product.discounted_price,
        risk_level=risk,
        confidence=round(confidence, 2)
    )

    db.add(new_prediction)
    db.commit()
    db.refresh(new_prediction)
    db.close()

    return {
        "RiskLevel": risk,
        "Confidence": round(confidence, 2)
    }
@app.get("/history")
def get_history():

    db = SessionLocal()

    predictions = (
        db.query(Prediction)
        .order_by(Prediction.id.desc())
        .limit(20)
        .all()
    )

    result = []

    for p in predictions:
        result.append({
            "id": p.id,
            "discount_percentage": p.discount_percentage,
            "rating": p.rating,
            "rating_count": p.rating_count,
            "actual_price": p.actual_price,
            "discounted_price": p.discounted_price,
            "risk_level": p.risk_level,
            "confidence": p.confidence,
            "created_at": p.created_at
        })

    db.close()

    return result