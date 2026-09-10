from pydantic import BaseModel, ConfigDict

from app.schemes.comments import CommentSchema


class ResponseManyPostsSchema(BaseModel):
    title: list[str]
    id: list[int]


class OnePostSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    title: str
    content: str
    comments: list[CommentSchema]


class CreatePostSchema(BaseModel):
    title: str
    content: str
