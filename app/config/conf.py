from pydantic_settings import BaseSettings

from app.config.jwt_conf import JWTConfig
from app.config.db_conf import DBConfig
from app.config.s3_conf import S3Config
from app.config.ai_conf import AIConfig
from app.config.redis_conf import RedisConfig


class Settings(BaseSettings):
    jwt_conf: JWTConfig = JWTConfig()
    s3_conf: S3Config = S3Config()
    db_conf: DBConfig = DBConfig()
    ai_conf: AIConfig = AIConfig()
    redis_conf: RedisConfig = RedisConfig()


settings = Settings()
