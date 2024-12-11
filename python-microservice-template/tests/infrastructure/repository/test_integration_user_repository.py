import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, clear_mappers, Session
from app.infrastructure.orm.entities_orm import Base, UserOrm
from app.infrastructure.repository.user_command_repository import ProductRepository
from app.domain.entities import User
from app.domain.exceptions import UserAlreadyExists
import uuid

DATABASE_URL = "sqlite:///:memory:"

@pytest.fixture(scope='function')
def session(): # type: ignore
    engine = create_engine(DATABASE_URL)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    yield session
    session.close()
    Base.metadata.drop_all(engine)
    engine.dispose()

@pytest.fixture
def repository(session: Session) -> ProductRepository:
    return ProductRepository(db=session)
    
def test_when_creating_user_then_user_is_created(repository: ProductRepository, session: Session) -> None:
    user = User(email="test@example.com", password="password123")
    created_user = repository.create(user)
    assert created_user.email == "test@example.com"
    assert created_user.password == "password123"

def test_when_creating_user_that_already_exists_then_raises_exception(repository: ProductRepository, session: Session) -> None:
    user = User(email="duplicate@example.com", password="password123")
    repository.create(user)
    with pytest.raises(UserAlreadyExists):
        repository.create(user)

def test_when_finding_user_by_id_then_user_is_found(repository: ProductRepository, session: Session) -> None:
    user = User(email="findme@example.com", password="password123")
    created_user = repository.create(user)
    found_user = repository.find_by_id(created_user.id)
    assert found_user is not None
    assert found_user.email == "findme@example.com"

def test_when_finding_user_by_id_that_does_not_exist_then_none_is_returned(repository: ProductRepository, session: Session) -> None:
    found_user = repository.find_by_id(str(uuid.uuid4()))
    assert found_user is None

def test_when_finding_user_by_email_then_user_is_found(repository: ProductRepository, session: Session) -> None:
    user = User(email="findbyemail@example.com", password="password123")
    repository.create(user)
    found_user = repository.find_by_email("findbyemail@example.com")
    assert found_user is not None
    assert found_user.email == "findbyemail@example.com"

def test_when_finding_user_by_email_that_does_not_exist_then_none_is_returned(repository: ProductRepository, session: Session) -> None:
    found_user = repository.find_by_email("nonexistent@example.com")
    assert found_user is None