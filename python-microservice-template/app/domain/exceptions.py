from enum import Enum


class ErrorCode(Enum):
    USER_NOT_FOUND = "USER_NOT_FOUND"
    USER_ALREADY_EXISTS = "USER_ALREADY_EXISTS"
    INVALID_CREDENTIALS = "INVALID_CREDENTIALS"
    INVALID_EMAIL = "INVALID_EMAIL"


class DomainException(Exception):
    def __init__(self, code: ErrorCode, message: str) -> None:
        self.code = code
        self.message = message
        super().__init__(code)


class UserNotFound(DomainException):
    def __init__(self, message: str | None = None) -> None:
        message = message if message else "User not found"
        super().__init__(ErrorCode.USER_NOT_FOUND, message)


class UserAlreadyExists(DomainException):
    def __init__(self, message: str | None = None) -> None:
        message = message if message else "User already exists"
        super().__init__(ErrorCode.USER_ALREADY_EXISTS, message)


class InvalidCredentials(DomainException):
    def __init__(self, message: str | None = None) -> None:
        message = message if message else "Invalid username or password"
        super().__init__(ErrorCode.INVALID_CREDENTIALS, message)
