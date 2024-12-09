from app.infrastructure.repository.user_command_repository import UserRepository
from app.domain.entities import RegistrationRequest, User
from app.utils.hashing import hash_password


class RegisterUser:
    def __init__(self, user_repository: UserRepository):
        self.user_repository: UserRepository = user_repository

    def execute(self, registration_request: RegistrationRequest) -> User:
        user: User = User(
            registration_request.email, hash_password(registration_request.password)
        )
        return self.user_repository.create(user)
