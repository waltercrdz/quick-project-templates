import logging

from src.persistence.queries import PRODUCT_INSERT
from src.domain.product import Product
from src.domain.error import DatabaseExecutionException, ProductAlreadyExistsException
from mysql.connector.errors import IntegrityError
from mysql.connector.pooling import PooledMySQLConnection

logger = logging.getLogger(__name__)

class ProductRepository:
    
    def __init__(self, connection: PooledMySQLConnection) -> None:
        self._connection = connection
    
    def save(self, product: Product) -> None:
        """Save a Product into the database"""
        logger.debug(f"Persisting a new {str(product)}")
        try:
            with self._connection.cursor() as _cursor:
                _cursor.execute(PRODUCT_INSERT, {
                    "id": str(product.id),
                    "name": product.name,
                    "description": product.description,
                    "price": product.price,
                    "stock": product.stock
                })
            self._connection.commit()
        except IntegrityError as e:
            self._connection.rollback()
            raise ProductAlreadyExistsException() from e
        except Exception as e:
            self._connection.rollback()
            raise DatabaseExecutionException() from e