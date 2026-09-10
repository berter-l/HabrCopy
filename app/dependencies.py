import jwt
from fastapi import Depends, WebSocketException
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from starlette import status

from app.services.authentication import get_decoded_token_data
from app.models.database import async_session

security = HTTPBearer()


async def get_user_id(
    security: HTTPAuthorizationCredentials = Depends(security),
) -> str:
    token_body = await get_decoded_token_data(security.credentials)

    return token_body["id"]


async def get_async_session():
    try:
        new_session = async_session()

        yield new_session

    except:
        await new_session.rollback()
        raise

    finally:
        await new_session.close()


async def get_ws_user_id(access_token: str) -> str:
    try:
        token_body = await get_decoded_token_data(access_token)

        return token_body["id"]

    except jwt.ExpiredSignatureError:
        raise WebSocketException(code=status.WS_1008_POLICY_VIOLATION)

    except jwt.InvalidTokenError:
        raise WebSocketException(code=status.WS_1008_POLICY_VIOLATION)
