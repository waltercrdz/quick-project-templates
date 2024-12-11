import uuid
import pytest
from sqlalchemy.orm import Session
from unittest.mock import Mock
from app.domain.entities import User
from app.domain.exceptions import UserAlreadyExists
from app.infrastructure.repository.user_command_repository import ProductRepository
from app.infrastructure.orm.entities_orm import UserOrm

USER_ID = str(uuid.uuid4())

@pytest.fixture
def db_session() -> Session:
    return Mock(spec=Session)

@pytest.fixture
def user_repository(db_session: Session) -> ProductRepository:
    return ProductRepository(db=db_session)

def test_create_user_success(user_repository: ProductRepository, db_session: Mock) -> None:
    # Arrange
    user = User(email="test@example.com", password="password123")
    db_session.query().filter().first.return_value = None

    # Act
    created_user = user_repository.create(user)

    # Assert
    db_session.add.assert_called_once()
    db_session.commit.assert_called_once()
    db_session.refresh.assert_called_once()
    assert created_user.email == user.email

def test_create_user_already_exists(user_repository: ProductRepository, db_session: Mock) -> None:
    # Arrange
    user = User(email="test@example.com", password="password123")
    db_session.query().filter().first.return_value = UserOrm(email=user.email, password=user.password)

    # Act & Assert
    with pytest.raises(UserAlreadyExists):
        user_repository.create(user)

def test_find_by_id(user_repository: ProductRepository, db_session: Mock) -> None:
    # Arrange
    user_orm = UserOrm(id=uuid.UUID(USER_ID), email="test@example.com", password="password123")
    db_session.query().filter().first.return_value = user_orm

    # Act
    user = user_repository.find_by_id(USER_ID)

    # Assert
    assert user is not None
    assert user.email == user_orm.email

def test_find_by_id_not_found(user_repository: ProductRepository, db_session: Mock) -> None:
    # Arrange
    db_session.query().filter().first.return_value = None

    # Act
    user = user_repository.find_by_id(USER_ID)

    # Assert
    assert user is None

def test_find_by_email(user_repository: ProductRepository, db_session: Mock) -> None:
    # Arrange
    email = "test@example.com"
    user_orm = UserOrm(email=email, password="password123")
    db_session.query().filter().first.return_value = user_orm

    # Act
    user = user_repository.find_by_email(email)

    # Assert
    assert user is not None
    assert user.email == user_orm.email

def test_find_by_email_not_found(user_repository: ProductRepository, db_session: Mock) -> None:
    # Arrange
    email = "test@example.com"
    db_session.query().filter().first.return_value = None

    # Act
    user = user_repository.find_by_email(email)

    # Assert
    assert user is None