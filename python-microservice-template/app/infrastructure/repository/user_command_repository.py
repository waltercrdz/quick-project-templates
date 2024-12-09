from uuid import UUID
from sqlalchemy.orm import Session
from app.domain.entities import User
from app.domain.exceptions import UserAlreadyExists
from app.infrastructure.orm.mappers import orm_to_user
from app.infrastructure.orm.entities_orm import UserOrm


class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, user: User) -> User:
        existing_user: User | None = self.find_by_email(user.email)
        if existing_user:
            raise UserAlreadyExists(f"User {user.email} already exists")

        user_orm: UserOrm = UserOrm(email=user.email, password=user.password)
        self.db.add(user_orm)
        self.db.commit()
        self.db.refresh(user_orm)
        return orm_to_user(user_orm)

    def find_by_id(self, user_id: str) -> User | None:
        user_orm: UserOrm | None = (
            self.db.query(UserOrm).filter(UserOrm.id == UUID(user_id)).first()
        )
        return orm_to_user(user_orm) if user_orm is not None else None

    def find_by_email(self, email: str) -> User | None:
        user_orm: UserOrm | None = (
            self.db.query(UserOrm).filter(UserOrm.email == email).first()
        )
        return orm_to_user(user_orm) if user_orm is not None else None
