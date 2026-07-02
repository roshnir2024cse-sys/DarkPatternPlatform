from pydantic import BaseModel

class ProductInput(BaseModel):
    discount_percentage: float
    rating: float
    rating_count: float
    actual_price: float
    discounted_price: float