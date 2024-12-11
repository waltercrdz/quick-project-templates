import logging
from app.domain.product import Product
from app.infrastructure.repository.product_repository import ProductRepository

logger = logging.getLogger(__name__)

class AddProduct:

    def __init__(self, repository: ProductRepository) -> None:
        self._repository = repository

    def execute(self, product: Product) -> None:
        logger.info(f"Creating new Product: {product}")
        self._repository.save(product)
        