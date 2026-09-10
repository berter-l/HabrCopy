from app.config.conf import settings
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase

USERNAME = settings.db_conf.username

HOST = settings.db_conf.host

PASSWORD = settings.db_conf.password

PORT = settings.db_conf.port

DB_NAME = settings.db_conf.db_name


async_engine = create_async_engine(
    f"postgresql+asyncpg://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DB_NAME}"
)

async_session = async_sessionmaker(async_engine)


class Base(DeclarativeBase):
    pass
