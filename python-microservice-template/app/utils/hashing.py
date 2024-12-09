from passlib.context import CryptContext

PWD_CONTEXT = CryptContext(schemes=["scrypt"], deprecated="auto")


def hash_password(password: str) -> str:
    hashed: str = PWD_CONTEXT.hash(password)
    return hashed


def verify_password(plain_password: str, hashed_password: str) -> bool:
    response: bool = PWD_CONTEXT.verify(plain_password, hashed_password)
    return response
