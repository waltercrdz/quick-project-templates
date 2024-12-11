from uuid import UUID
from app.domain.exceptions import ProductNotFoundException
from app.infrastructure.repository.product_repository import ProductRepository
from app.domain.product import Product


class FindProductById:
    def __init__(self, repository: ProductRepository):
        self._repository = repository

    def execute(self, product_id: UUID) -> Product:
        product: Product | None = self._repository.find_by_id(product_id)
        if product is None:
            raise ProductNotFoundException(f"Product with id {product_id} not found")
        return product
