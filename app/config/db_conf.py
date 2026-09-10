from pydantic import BaseModel


class DBConfig(BaseModel):
    host: str = "db"
    port: int = "5432"
    username: str = "test_app"
    password: str = "1234"
    db_name: str = "test_app"
