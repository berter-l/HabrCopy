from fastapi import APIRouter, Response, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status
from app.services.authentication import (
    register_user as service_register_user,
    login_user as service_login_user,
)

from app.schemes.authentication import (
    LoginCredentialsSchema,
    ResponseJWTTokensSchema,
    RegisterCredentialsSchema,
    RequestUpdateTokenSchema,
    ResponseUpdateTokenSchema,
)
from app.services.authentication import get_jwt_tokens, get_new_access_token
from app.dependencies import get_async_session

router = APIRouter()


@router.post("/auth/tokens/")
async def login_user(
    login_credentials: LoginCredentialsSchema,
    response: Response,
    session: AsyncSession = Depends(get_async_session),
) -> ResponseJWTTokensSchema:

    jwt_tokens = await service_login_user(
        login_credentials.email, login_credentials.password, session
    )

    response.status_code = status.HTTP_200_OK

    return jwt_tokens


@router.post("/auth/register/")
async def register_user(
    registration_details: RegisterCredentialsSchema,
    response: Response,
    session: AsyncSession = Depends(get_async_session),
) -> ResponseJWTTokensSchema:

    jwt_tokens = await service_register_user(
        registration_details.email,
        registration_details.password,
        registration_details.username,
        session,
    )

    response.status_code = status.HTTP_200_OK

    return jwt_tokens


@router.post("/auth/refresh_token/")
async def update_access_token(
    refresh_token: RequestUpdateTokenSchema, response: Response
) -> ResponseUpdateTokenSchema:

    new_access_token = await get_new_access_token(refresh_token.refresh_token)

    response.status_code = status.HTTP_200_OK

    return ResponseUpdateTokenSchema(access_token=new_access_token)
