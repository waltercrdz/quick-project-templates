from fastapi import FastAPI
from app.domain.exceptions import UserAlreadyExists, UserNotFound, InvalidCredentials
from app.infrastructure.routers import users, authentication
from app.infrastructure.routers.exception_handlers import (
    user_already_exists_exception_handler,
    user_not_found_exception_handler,
    invalid_credentials_exception_handler,
)

app: FastAPI = FastAPI()

app.include_router(users.router)
app.include_router(authentication.router)

app.add_exception_handler(UserAlreadyExists, user_already_exists_exception_handler)  # type: ignore
app.add_exception_handler(UserNotFound, user_not_found_exception_handler)  # type: ignore
app.add_exception_handler(InvalidCredentials, invalid_credentials_exception_handler)  # type: ignore
