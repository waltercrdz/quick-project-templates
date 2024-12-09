import pytest
from unittest.mock import Mock, patch
from app.application.authenticate_user import AuthenticateUser
from app.domain.entities import User
from app.domain.exceptions import InvalidCredentials
from app.infrastructure.repository.user_command_repository import UserRepository

EXAMPLE_EMAIL: str = 'test@example.com'
EXAMPLE_PASSWORD: str = 'password'

@pytest.fixture
def user_repository() -> Mock:
    return Mock(spec=UserRepository)

@pytest.fixture
def authenticate_user(user_repository: Mock) -> AuthenticateUser:
    return AuthenticateUser(user_repository)

def test_when_credentials_are_valid_then_authentication_is_successful(authenticate_user: AuthenticateUser, user_repository: Mock) -> None:
    user = Mock(spec=User)
    user.is_password_valid.return_value = True
    user_repository.find_by_email.return_value = user
    with patch('app.application.authenticate_user.create_access_token', return_value='token') as mock_create_token:
        token = authenticate_user.execute(EXAMPLE_EMAIL, EXAMPLE_PASSWORD)
        assert token == 'token'
        user_repository.find_by_email.assert_called_once_with(EXAMPLE_EMAIL)
        user.is_password_valid.assert_called_once_with(EXAMPLE_PASSWORD)
        mock_create_token.assert_called_once_with(user)

def test_when_user_not_found_then_raise_invalid_credentials(authenticate_user: AuthenticateUser, user_repository: Mock) -> None:
    user_repository.find_by_email.return_value = None
    with pytest.raises(InvalidCredentials):
        authenticate_user.execute(EXAMPLE_EMAIL, EXAMPLE_PASSWORD)
    user_repository.find_by_email.assert_called_once_with(EXAMPLE_EMAIL)

def test_when_password_is_invalid_then_raise_invalid_credentials(authenticate_user: AuthenticateUser, user_repository: Mock) -> None:
    user = Mock(spec=User)
    user.is_password_valid.return_value = False
    user_repository.find_by_email.return_value = user
    with pytest.raises(InvalidCredentials):
        authenticate_user.execute(EXAMPLE_EMAIL, EXAMPLE_PASSWORD)
    user_repository.find_by_email.assert_called_once_with(EXAMPLE_EMAIL)
    user.is_password_valid.assert_called_once_with(EXAMPLE_PASSWORD)