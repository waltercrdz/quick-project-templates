from fastapi import Request
from fastapi.responses import JSONResponse
from pydantic import ValidationError
from app.domain.exceptions import (
    DatabaseExecutionException,
    DomainException,
    ProductAlreadyExistsException,
    ProductNotFoundException,
)

def create_json_response(status_code: int, exception: DomainException) -> JSONResponse:
    return JSONResponse(
        status_code=status_code,
        content={"code": exception.code.value, "message": exception.message},
    )

def create_json_response_from_exc(
        status_code: int, exception: Exception
) -> JSONResponse:
    return JSONResponse(
        status_code=status_code,
        content={"code": status_code, "message": str(exception)},
    )

async def product_already_exists_exception_handler(
    _: Request, exception: ProductAlreadyExistsException
) -> JSONResponse:
    return create_json_response(400, exception)


async def product_not_found_exception_handler(
    _: Request, exception: ProductNotFoundException
) -> JSONResponse:
    return create_json_response(404, exception)

async def database_execution_exception_handler(
    _: Request, exception: DatabaseExecutionException
) -> JSONResponse:
    return create_json_response(500, exception)

async def value_error_handler(
    _: Request, exception: ValueError
) -> JSONResponse:
    return create_json_response_from_exc(400, exception)

async def internal_server_error_handler(
    _: Request, exception: Exception
) -> JSONResponse:
    return create_json_response_from_exc(500, exception)
