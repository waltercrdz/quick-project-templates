import logging
from app.domain.entities import User
from app.domain.exceptions import InvalidCredentials
from app.infrastructure.repository.user_command_repository import UserRepository

from app.utils.token_generator import create_access_token

logger = logging.getLogger(__name__)


class AuthenticateUser:
    def __init__(self, user_repository: UserRepository) -> None:
        self.user_repository = user_repository

    def execute(self, email: str, password: str) -> str:
        logger.info(f"Authenticating user with email: {email}")
        user: User | None = self.user_repository.find_by_email(email)
        if user is None or not user.is_password_valid(password):
            raise InvalidCredentials()
        return create_access_token(user)
