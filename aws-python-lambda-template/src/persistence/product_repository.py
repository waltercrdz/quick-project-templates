import logging

from src.persistence.queries import PRODUCT_INSERT
from src.domain.product import Product
from src.domain.error import DatabaseExecutionException, ProductAlreadyExistsException
from psycopg2 import IntegrityError
from psycopg2.extensions import connection

logger = logging.getLogger(__name__)

class ProductRepository:
    
    def __init__(self, connection: connection) -> None:
        self._db_client = connection
        self._cursor = self._db_client.cursor()
    
    def save(self, product: Product) -> None:
        """Save a Product into the database"""
        logger.debug(f"Persisting a new {str(product)}")
        try:
            self._cursor.execute(PRODUCT_INSERT, {
                "id": product.id,
                "name": product.name,
                "description": product.description,
                "price": product.price,
                "stock": product.stock
            })
            return self._cursor.lastrowid
        except IntegrityError as e:
            raise ProductAlreadyExistsException(code=e) from e
        except Exception as e:
            raise DatabaseExecutionException(source=e) from e