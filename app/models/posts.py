from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, relationship
from sqlalchemy.orm import mapped_column

from app.models.database import Base


class Posts(Base):
    __tablename__ = "posts"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
    content: Mapped[str]
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"))
    user: Mapped["Users"] = relationship("Users", back_populates="user_posts")
    comments: Mapped[list["Comments"]] = relationship("Comments", back_populates="post")
