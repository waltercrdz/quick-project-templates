from dataclasses import dataclass
from app.utils.hashing import verify_password


@dataclass
class RegistrationRequest:
    email: str
    password: str


@dataclass
class AuthenticationRequest:
    email: str
    password: str
    type: str | None = None


class User:
    _id: str | None
    _email: str
    _password: str

    def __init__(self, email: str, password: str, user_id: str | None = None):
        self._id = user_id
        self._email = email
        self._password = password

    @property
    def id(self) -> str | None:
        return self._id

    @property
    def email(self) -> str:
        return self._email

    @property
    def password(self) -> str:
        return self._password

    def is_password_valid(self, password: str) -> bool:
        return verify_password(password, self._password)

    def to_dict(self) -> dict[str, str]:
        return {
            "id": self._id,  # type: ignore
            "email": self._email,
        }
    
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, User):
            return NotImplemented
        return self._id == other._id and self._email == other._email
