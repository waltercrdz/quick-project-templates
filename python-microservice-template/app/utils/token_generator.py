from typing import Any
import jwt
import os
from datetime import datetime, timedelta, timezone
from app.domain.entities import User

SECRET_KEY: str = os.getenv("SECRET_KEY", "secret")
ALGORITHM: str = os.getenv("ALGORITHM", "HS256")
ACCESS_TOKEN_EXPIRE_MINUTES: int = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 15))


def create_access_token(user: User) -> str:
    expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    payload: dict[str, Any] = {
        "iat": datetime.now(timezone.utc),
        "sub": user._email,
        "exp": expire,
        "user_id": user._id,
    }
    encoded_jwt = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt
