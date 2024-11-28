import logging
import os
from typing import Generator
from mysql.connector.pooling import MySQLConnectionPool
from mysql.connector.pooling import PooledMySQLConnection

from contextlib import contextmanager

from src.persistence.product_repository import ProductRepository
from src.application.add_product import AddProduct

# DB
DB_HOST: str | None = os.environ.get("DB_HOST")
DB_USER: str | None = os.environ.get("DB_USER")
DB_PASSWORD: str | None = os.environ.get("DB_PASSWORD")
DB_NAME: str | None = os.environ.get("DB_NAME")

# Logging configuration
root = logging.getLogger()
if root.handlers:
    for handler in root.handlers:
        root.removeHandler(handler)
logging.basicConfig(
    format="%(levelname)s - %(asctime)s - %(message)s",
    datefmt="%Y-%m-%dT%H:%M:%S",
    level=logging.INFO)

# Initialize the connection pool
_CONNECTION_POOL: MySQLConnectionPool = MySQLConnectionPool(
    pool_name="product_pool",
    pool_size=10,
    pool_reset_session=True,
    host=DB_HOST,
    user=DB_USER,
    password=DB_PASSWORD,
    database=DB_NAME
)

def get_connection() -> PooledMySQLConnection:
    return _CONNECTION_POOL.get_connection()

def release_connection(connection: PooledMySQLConnection) -> None:
    connection.close()

@contextmanager
def create_add_product() -> Generator[AddProduct, None, None]:
    """
    Context manager to create AddProduct with proper connection management.
    Ensures the connection is released after use.
    """
    connection:PooledMySQLConnection = get_connection()
    try:
        repository = ProductRepository(connection=connection)
        yield AddProduct(repository=repository)
    finally:
        release_connection(connection)