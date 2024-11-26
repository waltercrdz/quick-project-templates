import logging
from src.domain.product import Product
from src.persistence.product_repository import ProductRepository

logger = logging.getLogger(__name__)

class AddProduct:

    def __init__(self, repository: ProductRepository) -> None:
        self._repository = repository

    def execute(self, product: Product) -> None:
        self._repository.save(product)
        