from fastapi import APIRouter, Depends
from app.application.find_user_by_id import FindUserById
from app.configuration.config import get_user_finder, get_register_user
from app.domain.entities import RegistrationRequest
from app.application.register_user import RegisterUser

router = APIRouter(
    prefix="/users",
    tags=["users"],
    responses={404: {"description": "Not found"}},
)


@router.post(
    "/",
    tags=["custom"],
    responses={403: {"description": "Operation forbidden"}},
)
async def register(
    registration_request: RegistrationRequest,
    register_user: RegisterUser = Depends(get_register_user),
) -> dict[str, str]:
    return register_user.execute(registration_request).to_dict()


@router.get(
    "/{user_id}",
    tags=["custom"],
    responses={403: {"description": "Operation forbidden"}},
)
async def get_user(
    user_id: str, user_finder: FindUserById = Depends(get_user_finder)
) -> dict[str, str]:
    return user_finder.execute(user_id).to_dict()
