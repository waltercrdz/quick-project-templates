from uuid import UUID
from decimal import Decimal
from app.domain.product import Product
from app.infrastructure.routers.dto import ProductCreationRequest

PRODUCT_ID = UUID("123e4567-e89b-12d3-a456-426614174000")
PRODUCT_NAME = "Test Product"
PRODUCT_DESCRIPTION = "Test Description"
PRODUCT_PRICE = Decimal(100)
PRODUCT_STOCK = 10

class ProductCreationRequestObjectMother:
    @staticmethod
    def create() -> ProductCreationRequest:
        return ProductCreationRequest(
            name=PRODUCT_NAME,
            description=PRODUCT_DESCRIPTION,
            price=PRODUCT_PRICE,
            stock=PRODUCT_STOCK
        )

class ProductObjectMother:
    @staticmethod
    def create() -> Product:
        return Product(
            id=PRODUCT_ID,
            name=PRODUCT_NAME,
            description=PRODUCT_DESCRIPTION,
            price=PRODUCT_PRICE,
            stock=PRODUCT_STOCK
        )