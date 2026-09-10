from sqlalchemy import ForeignKey

from sqlalchemy.orm import Mapped, relationship
from sqlalchemy.orm import mapped_column

from app.models.database import Base


class Comments(Base):
    __tablename__ = "comments"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"))
    comment_content: Mapped[str]
    post_id: Mapped[int] = mapped_column(ForeignKey("posts.id", ondelete="CASCADE"))
    post: Mapped["Posts"] = relationship(back_populates="comments")
