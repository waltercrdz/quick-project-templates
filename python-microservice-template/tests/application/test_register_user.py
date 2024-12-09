import pytest
from unittest.mock import Mock
from app.application.register_user import RegisterUser
from app.domain.entities import RegistrationRequest, User
from app.domain.exceptions import UserAlreadyExists
from app.infrastructure.repository.user_command_repository import UserRepository
from app.utils.hashing import hash_password

USER_EMAIL: str = "test@example.com"
PASSWORD: str = "password"
HASHED_PASSWORD: str = hash_password(PASSWORD)

@pytest.fixture
def user_repository() -> Mock:
    return Mock(spec=UserRepository)

@pytest.fixture
def register_user(user_repository: Mock) -> RegisterUser:
    return RegisterUser(user_repository)

def test_when_registration_is_successful_then_return_user(register_user: RegisterUser, user_repository: Mock) -> None:
    registration_request: RegistrationRequest = RegistrationRequest(USER_EMAIL, PASSWORD)
    user: User = User(USER_EMAIL, HASHED_PASSWORD)
    user_repository.create.return_value = user
    result = register_user.execute(registration_request)
    assert result == user
    user_repository.create.assert_called_once_with(user)

def test_when_registration_fails_then_raise_exception(register_user: RegisterUser, user_repository: Mock) -> None:
    registration_request: RegistrationRequest = RegistrationRequest(USER_EMAIL, PASSWORD)
    user_repository.create.side_effect = UserAlreadyExists()
    with pytest.raises(UserAlreadyExists):
        register_user.execute(registration_request)
    user_repository.create.assert_called_once()