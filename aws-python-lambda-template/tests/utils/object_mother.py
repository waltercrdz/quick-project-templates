from uuid import UUID
from decimal import Decimal
from src.domain.product import Product

class ProductObjectMother:
    @staticmethod
    def create_product() -> Product:
        return Product(
            id=UUID("123e4567-e89b-12d3-a456-426614174000"),
            name="Test Product",
            description="Test Description",
            price=Decimal(100),
            stock=10
        )