import json
from uuid import UUID

from src.shared.mappers import map_to_product
from src.domain.product import Product

def test_map_to_product():
    record = {
        "body": json.dumps({
            "id": "123e4567-e89b-12d3-a456-426614174000",
            "name": "Product 1",
            "description": "Product 1 description",
            "price": 1.0,
            "stock": 10
        })
    }

    product: Product = map_to_product(record)

    assert product.id == UUID("123e4567-e89b-12d3-a456-426614174000")
    assert product.name == "Product 1"
    assert product.description == "Product 1 description"
    assert product.price == 1.0
    assert product.stock == 10