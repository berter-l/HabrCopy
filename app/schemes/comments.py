from pydantic import BaseModel


class CommentSchema(BaseModel):
    comment_content: str
