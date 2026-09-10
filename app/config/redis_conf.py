from pydantic import BaseModel


class RedisConfig(BaseModel):
    server_name: str = "redis"
    port: int = 6379
