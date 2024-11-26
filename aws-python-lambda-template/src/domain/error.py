from enum import Enum

class ErrorCode(Enum):
    INVALID_JSON = "INVALID_JSON"
    BAD_REQUEST = "BAD_REQUEST"
    DATABASE_EXECUTION = "DATABASE_EXECUTION"
    PRODUCT_ALREADY_EXISTS = "DATABASE_EXECUTION"

class DomainException(Exception):
    def __init__(
            self,
            code: ErrorCode,
            message: str = "An unexpected error has ocurred!",
            source: Exception | None = None
    ):
        self.code = code
        self.message = message
        self.source = source
        super().__init__(self.message)

class InvalidInputException(DomainException):
    def __init__(
            self,
            code: ErrorCode = ErrorCode.BAD_REQUEST,
            message: str = "There are missing parameters in the request"
    ):
        super().__init__(code, message)

class DatabaseExecutionException(DomainException):
    def __init__(
            self,
            code: ErrorCode = ErrorCode.DATABASE_EXECUTION,
            message: str = "There was an error trying to execute a database operation",
            source: Exception | None = None):
        super().__init__(code, message, source)

class ProductAlreadyExistsException(DomainException):
    def __init__(
            self,
            code: ErrorCode = ErrorCode.PRODUCT_ALREADY_EXISTS,
            message: str = "The product already exists in the database",
            source: Exception | None = None):
        super().__init__(code, message, source)