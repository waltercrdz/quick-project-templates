import logging
import os
from typing import AsyncGenerator
from fastapi import FastAPI
from mysql.connector.pooling import MySQLConnectionPool

from app.application.add_product import AddProduct
from app.application.find_product_by_id import FindProductById
from app.infrastructure.persistence.product_repository import ProductRepository

from contextlib import asynccontextmanager

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

logger = logging.getLogger(__name__)

_CONNECTION_POOL: MySQLConnectionPool

@asynccontextmanager
async def lifespan(_: FastAPI) -> AsyncGenerator[None, None]:
    logger.info("Initializing the database connection pool...")
    global _CONNECTION_POOL
    _CONNECTION_POOL = MySQLConnectionPool(
        pool_name="product_pool",
        pool_size=10,
        pool_reset_session=True,
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
    )
    yield

def get_add_product() -> AddProduct:
    repository: ProductRepository = ProductRepository(connection_pool=_CONNECTION_POOL)
    return AddProduct(repository=repository)

def get_find_product_by_id() -> FindProductById:
    repository = ProductRepository(connection_pool=_CONNECTION_POOL)
    return FindProductById(repository=repository)