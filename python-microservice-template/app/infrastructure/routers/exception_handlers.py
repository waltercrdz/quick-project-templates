from fastapi import Request
from fastapi.responses import JSONResponse
from app.domain.exceptions import (
    DomainException,
    InvalidCredentials,
    UserAlreadyExists,
    UserNotFound,
)


async def user_already_exists_exception_handler(
    _: Request, exception: UserAlreadyExists
) -> JSONResponse:
    return create_json_response(400, exception)


async def user_not_found_exception_handler(
    _: Request, exception: UserNotFound
) -> JSONResponse:
    return create_json_response(404, exception)


async def invalid_credentials_exception_handler(
    _: Request, exception: InvalidCredentials
) -> JSONResponse:
    return create_json_response(401, exception)


def create_json_response(status_code: int, exception: DomainException) -> JSONResponse:
    return JSONResponse(
        status_code=status_code,
        content={"code": exception.code.value, "message": exception.message},
    )
