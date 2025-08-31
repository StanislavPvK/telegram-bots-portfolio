from pydantic import BaseModel
from typing import List

# модель товара
class Product(BaseModel):
    id: str
    title: str
    price: int
    file_path: str


# список доступных товаров
PRODUCTS: List[Product] = [
    Product(
        id="productivity",
        title="Чек-лист продуктивности",
        price=990,  # 9.9 USD -> 990 cents
        file_path="app/files/productivity.pdf"
    ),
    Product(
        id="nutrition",
        title="Чек-лист по питанию",
        price=1490,  # 14.9 USD
        file_path="app/files/nutrition.pdf"
    ),
    Product(
        id="planning",
        title="Чек-лист по планированию дня",
        price=1990,  # 19.9 USD
        file_path="app/files/planning.pdf"
    ),
]


# поиск товара по id
def get_product(product_id: str):
    for product in PRODUCTS:
        if product.id == product_id:
            return product
    return None