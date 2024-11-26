import logging
import os
from typing import Generator

from psycopg2.pool import SimpleConnectionPool
from psycopg2.extensions import connection
from contextlib import contextmanager

from src.persistence.product_repository import ProductRepository
from src.application.add_product import AddProduct

# DB
DB_HOST: str = os.environ.get("DB_HOST")
DB_USER: str = os.environ.get("DB_USER")
DB_PASSWORD: str = os.environ.get("DB_PASSWORD")
DB_NAME: str = os.environ.get("DB_NAME")

# Logging configuration
root = logging.getLogger()
if root.handlers:
    for handler in root.handlers:
        root.removeHandler(handler)
logging.basicConfig(
    format="%(levelname)s - %(asctime)s - %(message)s",
    datefmt="%Y-%m-%dT%H:%M:%S",
    level=logging.INFO
)

# Global variables
_ADD_PRODUCT_UC: AddProduct | None = None

# Initialize the connection pool
_CONNECTION_POOL: SimpleConnectionPool = SimpleConnectionPool(
    minconn=1,
    maxconn=10,
    user=DB_USER,
    password=DB_PASSWORD,
    host=DB_HOST,
    database=DB_NAME
)

def get_connection() -> connection:
    return _CONNECTION_POOL.getconn()

def release_connection(connection: connection) -> None:
    _CONNECTION_POOL.putconn(connection)

@contextmanager
def create_add_product() -> Generator[AddProduct, None, None]:
    """
    Context manager to create AddProduct with proper connection management.
    Ensures the connection is released after use.
    """
    connection = get_connection()
    try:
        repository = ProductRepository(connection=connection)
        yield AddProduct(repository=repository)
    finally:
        release_connection(connection)