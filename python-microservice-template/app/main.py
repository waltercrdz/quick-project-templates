from fastapi import FastAPI
from pydantic import ValidationError
from app.domain.exceptions import DatabaseExecutionException, ProductAlreadyExistsException, ProductNotFoundException
from app.infrastructure.routers import products
from app.configuration.config import lifespan
from app.infrastructure.routers.exception_handlers import (
    product_already_exists_exception_handler,
    product_not_found_exception_handler,
    database_execution_exception_handler,
    internal_server_error_handler,
    value_error_handler
)

app: FastAPI = FastAPI(lifespan=lifespan)

app.include_router(products.router)

app.add_exception_handler(
    ProductAlreadyExistsException,
    product_already_exists_exception_handler # type: ignore
)

app.add_exception_handler(
    ProductNotFoundException, 
    product_not_found_exception_handler # type: ignore
)

app.add_exception_handler(
    DatabaseExecutionException, 
    database_execution_exception_handler # type: ignore
)

app.add_exception_handler(
    ValueError, 
    value_error_handler # type: ignore
)

app.add_exception_handler(
    Exception, 
    internal_server_error_handler
)
