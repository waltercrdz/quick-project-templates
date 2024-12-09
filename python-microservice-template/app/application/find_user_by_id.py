from app.domain.entities import User
from app.domain.exceptions import UserNotFound
from app.infrastructure.repository.user_command_repository import UserRepository


class FindUserById:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def execute(self, user_id: str) -> User:
        user: User | None = self.user_repository.find_by_id(user_id)
        if user is None:
            raise UserNotFound(f"User with id {user_id} not found")
        return user
