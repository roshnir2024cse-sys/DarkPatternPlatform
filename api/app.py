from fastapi import FastAPI
from pathlib import Path
from api.schemas import ProductInput
import joblib
import pandas as pd
from fastapi.middleware.cors import CORSMiddleware
import sqlite3


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

    # -------------------------
    # Save Prediction to SQLite
    # -------------------------

    conn = sqlite3.connect(DB_PATH)

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS predictions (

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

    cursor.execute("""
    INSERT INTO predictions (

        discount_percentage,
        rating,
        rating_count,
        actual_price,
        discounted_price,
        risk_level,
        confidence

    )

    VALUES (?, ?, ?, ?, ?, ?, ?)

    """, (

        product.discount_percentage,
        product.rating,
        product.rating_count,
        product.actual_price,
        product.discounted_price,

        risk,
        round(confidence, 2)

    ))

    conn.commit()

    conn.close()

    return {
        "RiskLevel": risk,
        "Confidence": round(confidence, 2)
    }
@app.get("/history")
def get_history():

    conn = sqlite3.connect(DB_PATH)

    conn.row_factory = sqlite3.Row

    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            id,
            discount_percentage,
            rating,
            rating_count,
            actual_price,
            discounted_price,
            risk_level,
            confidence,
            created_at
        FROM predictions
        ORDER BY id DESC
        LIMIT 20
    """)

    rows = cursor.fetchall()

    conn.close()

    return [dict(row) for row in rows]