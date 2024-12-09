from fastapi import APIRouter, Depends
from app.application.authenticate_user import AuthenticateUser
from app.configuration.config import get_authenticate_user
from app.domain.entities import AuthenticationRequest

router = APIRouter(
    prefix="/auth",
    tags=["auth"],
    responses={401: {"description": "Unauthorized"}},
)


@router.post(
    "/",
    tags=["custom"],
    responses={403: {"description": "Operation forbidden"}},
)
async def authenticate(
    authentication_request: AuthenticationRequest,
    authenticate_user: AuthenticateUser = Depends(get_authenticate_user),
) -> dict[str, str]:
    return {
        "token": authenticate_user.execute(
            authentication_request.email, authentication_request.password
        )
    }
