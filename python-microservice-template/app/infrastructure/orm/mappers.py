from app.domain.entities import User
from app.infrastructure.orm.entities_orm import UserOrm


def orm_to_user(user_orm: UserOrm) -> User:
    return User(
        user_id=str(user_orm.id),
        email=str(user_orm.email),
        password=str(user_orm.password),
    )
