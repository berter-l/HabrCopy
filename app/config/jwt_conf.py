from pydantic import BaseModel


class JWTConfig(BaseModel):
    algorithm: str = "HS256"
    secret_key: str = "fe2179e0-69cd-443d-b757-f5e477cce0d7"
    refresh_token_ttl_minute: int = 7 * 24 * 60
    access_token_ttl_minute: int = 10
