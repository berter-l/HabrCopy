from sqlalchemy.orm import Mapped, relationship
from sqlalchemy.orm import mapped_column

from app.models.database import Base


class Users(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(unique=True)
    username: Mapped[str] = mapped_column(unique=True)
    password: Mapped[str]
    user_posts: Mapped[list["Posts"]] = relationship("Posts", back_populates="user")
