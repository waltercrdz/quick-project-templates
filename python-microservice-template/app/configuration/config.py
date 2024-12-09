import logging
import os

from app.application.authenticate_user import AuthenticateUser
from app.application.register_user import RegisterUser
from app.application.find_user_by_id import FindUserById
from app.infrastructure.repository.user_command_repository import UserRepository
from app.configuration.database import SessionLocal, engine
from app.infrastructure.orm.entities_orm import Base

# Environment variables
DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///./test.db")

# Logging configuration
root = logging.getLogger()
if root.handlers:
    for handler in root.handlers:
        root.removeHandler(handler)
logging.basicConfig(
    format="%(levelname)s - %(asctime)s - %(message)s",
    datefmt="%Y-%m-%dT%H:%M:%S",
    level=logging.INFO,
)

logger = logging.getLogger(__name__)


# Dependency Injection
def get_register_user() -> RegisterUser:
    session = SessionLocal()
    user_repository: UserRepository = UserRepository(session)
    return RegisterUser(user_repository)


def get_user_finder() -> FindUserById:
    session = SessionLocal()
    user_repository: UserRepository = UserRepository(session)
    return FindUserById(user_repository)


def get_authenticate_user() -> AuthenticateUser:
    session = SessionLocal()
    user_repository: UserRepository = UserRepository(session)
    return AuthenticateUser(user_repository)
