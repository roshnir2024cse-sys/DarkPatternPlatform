from sqlalchemy import Column, Integer, Float, String, DateTime
from sqlalchemy.orm import declarative_base
from sqlalchemy.sql import func

Base = declarative_base()

class Prediction(Base):
    __tablename__ = "predictions"

    id = Column(Integer, primary_key=True, index=True)

    discount_percentage = Column(Float)
    rating = Column(Float)
    rating_count = Column(Float)
    actual_price = Column(Float)
    discounted_price = Column(Float)

    risk_level = Column(String)
    confidence = Column(Float)

    created_at = Column(DateTime(timezone=True), server_default=func.now())