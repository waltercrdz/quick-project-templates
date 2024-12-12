
from decimal import Decimal
from uuid import UUID
from app.domain.product import Product
from app.infrastructure.routers.dto import ProductCreationRequest

def map_to_product(
    product_creation_request: ProductCreationRequest, 
    product_id: UUID
) -> Product:
    return Product(
        id=product_id,
        name=product_creation_request.name,
        description=product_creation_request.description,
        price=Decimal(product_creation_request.price),
        stock=product_creation_request.stock
    )