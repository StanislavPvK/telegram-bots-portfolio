from pydantic import BaseModel
from typing import List

# Product model
class Product(BaseModel):
    id: str
    title: str
    price: int
    file_path: str


# List of available products
PRODUCTS: List[Product] = [
    Product(
        id="productivity",
        title="Productivity Checklist",
        price=990,  # 9.9 USD -> 990 cents
        file_path="app/files/productivity.pdf"
    ),
    Product(
        id="nutrition",
        title="Nutrition Checklist",
        price=1490,  # 14.9 USD
        file_path="app/files/nutrition.pdf"
    ),
    Product(
        id="planning",
        title="Daily Planning Checklist",
        price=1990,  # 19.9 USD
        file_path="app/files/planning.pdf"
    ),
]


# Find a product by id
def get_product(product_id: str):
    for product in PRODUCTS:
        if product.id == product_id:
            return product
    return None
