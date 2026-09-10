from asyncio import to_thread
from datetime import timedelta, datetime, timezone
from typing import Any
import bcrypt
import jwt
from fastapi import HTTPException
from jwt import encode, decode
from pydantic import EmailStr
from sqlalchemy import select, or_
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from app.config.conf import settings
from app.schemes.authentication import ResponseJWTTokensSchema
from app.models.users import Users


async def get_jwt_tokens(token_body: dict) -> ResponseJWTTokensSchema:
    refresh_token = await create_jwt_token(token_body, "refresh")

    access_token = await create_jwt_token(token_body, "access")

    return ResponseJWTTokensSchema(
        refresh_token=refresh_token, access_token=access_token
    )


async def get_decoded_token_data(jwt_token: str) -> dict:
    try:
        token_body = await to_thread(
            decode, jwt_token, settings.jwt_conf.secret_key, settings.jwt_conf.algorithm
        )
        return token_body

    except jwt.ExpiredSignatureError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token expired. Please log in again.",
        )
    except jwt.InvalidTokenError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid token",
        )


async def create_jwt_token(body: dict, token_type: str) -> Any:
    token_ttl = (
        settings.jwt_conf.access_token_ttl_minute
        if token_type == "access"
        else settings.jwt_conf.refresh_token_ttl_minute
    )

    body["exp"] = datetime.now(tz=timezone.utc) + timedelta(minutes=token_ttl)

    token = await to_thread(
        encode, body, settings.jwt_conf.secret_key, settings.jwt_conf.algorithm
    )

    return token


async def get_new_access_token(refresh_token: str) -> str:
    token_body = await get_decoded_token_data(refresh_token)

    new_access_token = await create_jwt_token(token_body, "access")

    return new_access_token


async def create_user(
    email: EmailStr, hash_password: str, username, session: AsyncSession
) -> Any:
    user = Users(email=email, password=hash_password, username=username)

    session.add(user)

    await session.commit()

    await session.refresh(user)

    return user


async def get_user(filter: dict, session: AsyncSession) -> Any:
    user_query = select(Users).filter_by(**filter)

    user = await session.scalar(user_query)

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
        )

    return user


async def get_hash_password(password: bytes) -> bytes:
    salt = bcrypt.gensalt()

    hashed_password = await to_thread(bcrypt.hashpw, password, salt)

    return hashed_password


async def verify_password(raw_password: bytes, hashed_password: bytes) -> bool:
    is_verify_password = await to_thread(bcrypt.checkpw, raw_password, hashed_password)

    return is_verify_password


async def register_user(
    user_email, user_password, username, session: AsyncSession
) -> Any:

    await check_if_the_user_exists(user_email, username, session)

    hash_password = await get_hash_password(user_password.encode())

    user = await create_user(
        email=user_email,
        hash_password=hash_password.decode("utf-8"),
        username=username,
        session=session,
    )

    body_jwt_tokens = {"id": user.id}

    jwt_tokens = await get_jwt_tokens(body_jwt_tokens)

    return jwt_tokens


async def login_user(email: EmailStr, password: str, session: AsyncSession) -> Any:
    user = await get_user({"email": email}, session)

    is_verify_password = await verify_password(
        password.encode(), user.password.encode()
    )
    if not is_verify_password:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
        )

    jwt_tokens = await get_jwt_tokens({"id": user.id})

    return jwt_tokens


async def check_if_the_user_exists(
    email: EmailStr, username: str, session: AsyncSession
):
    user_query = select(Users).where(
        or_(Users.email == email, Users.username == username)
    )
    user = await session.scalar(user_query)

    if user is None:
        return None

    raise HTTPException(
        status_code=status.HTTP_422_UNPROCESSABLE_CONTENT, detail="User exists"
    )
