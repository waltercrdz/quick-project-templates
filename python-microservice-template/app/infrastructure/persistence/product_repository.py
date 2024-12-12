import logging
from uuid import UUID

from app.infrastructure.persistence.queries import PRODUCT_INSERT, PRODUCT_SELECT_BY_ID
from app.domain.product import Product
from app.domain.exceptions import (
    DatabaseExecutionException,
    ProductAlreadyExistsException
)
from mysql.connector.errors import IntegrityError
from mysql.connector.pooling import PooledMySQLConnection
from mysql.connector.pooling import MySQLConnectionPool

logger = logging.getLogger(__name__)

class ProductRepository:
    
    def __init__(self, connection_pool: MySQLConnectionPool) -> None:
        self._connection_pool = connection_pool
    
    def save(self, product: Product) -> None:
        """Save a Product into the database"""
        logger.debug(f"Persisting a new {str(product)}")
        try:
            connection: PooledMySQLConnection = self._connection_pool.get_connection()
            with connection.cursor() as _cursor:
                _cursor.execute(PRODUCT_INSERT, {
                    "id": str(product.id),
                    "name": product.name,
                    "description": product.description,
                    "price": product.price,
                    "stock": product.stock
                })
            connection.commit()
        except IntegrityError as e:
            connection.rollback()
            raise ProductAlreadyExistsException() from e
        except Exception as e:
            connection.rollback()
            raise DatabaseExecutionException() from e
        finally:
            connection.close()
        
    def find_by_id(self, product_id: UUID) -> Product | None:
        """Find a Product by id"""
        logger.debug(f"Finding Product with id {product_id}")
        try:
            connection: PooledMySQLConnection = self._connection_pool.get_connection()
            with connection.cursor() as _cursor:
                _cursor.execute(PRODUCT_SELECT_BY_ID, {"id": str(product_id)})
                result = _cursor.fetchone()
                if result is None:
                    return None
                return Product(
                    id=result[0],
                    name=result[1],
                    description=result[2],
                    price=result[3],
                    stock=result[4],
                    created_at=result[5],
                    updated_at=result[6]
               )
        finally:
            connection.close()