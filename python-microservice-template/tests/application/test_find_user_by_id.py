import pytest
from unittest.mock import Mock
from app.application.find_user_by_id import FindUserById
from app.domain.entities import User
from app.domain.exceptions import UserNotFound
from app.infrastructure.repository.user_command_repository import ProductRepository

USER_ID: str = "1234"
USER_EMAIL: str = "test@example.com"
PASSWORD: str = "password"

@pytest.fixture
def user_repository() -> Mock:
    return Mock(spec=ProductRepository)

@pytest.fixture
def find_user_by_id(user_repository: Mock) -> FindUserById:
    return FindUserById(user_repository)

def test_when_user_is_found_then_return_user(find_user_by_id: FindUserById, user_repository: Mock) -> None:
    user: User = User(USER_ID, USER_EMAIL, PASSWORD)
    user_repository.find_by_id.return_value = user
    result = find_user_by_id.execute(USER_ID)
    assert result == user
    user_repository.find_by_id.assert_called_once_with(USER_ID)

def test_when_user_is_not_found_then_raise_user_not_found(find_user_by_id: FindUserById, user_repository: Mock) -> None:
    user_repository.find_by_id.return_value = None
    with pytest.raises(UserNotFound):
        find_user_by_id.execute(USER_ID)
    user_repository.find_by_id.assert_called_once_with(USER_ID)