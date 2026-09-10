from fastapi import APIRouter, Response, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status
from app.dependencies import get_user_id, get_async_session
from app.schemes.posts import ResponseManyPostsSchema, CreatePostSchema, OnePostSchema
from app.services.posts import (
    create_post as service_create_post,
    get_post_by_id,
    get_all_posts_title as service_get_all_posts_title,
)

router = APIRouter()


@router.get("/posts", response_model=ResponseManyPostsSchema)
async def get_all_posts(
    response: Response,
    user_id: int = Depends(get_user_id),
    session: AsyncSession = Depends(get_async_session),
) -> ResponseManyPostsSchema:

    posts = await service_get_all_posts_title(session)

    response.status_code = status.HTTP_200_OK

    return posts


@router.post("/posts")
async def create_post(
    post_data: CreatePostSchema,
    response: Response,
    session: AsyncSession = Depends(get_async_session),
    user_id: int = Depends(get_user_id),
) -> Response:

    await service_create_post(post_data.title, post_data.content, user_id, session)

    response.status_code = status.HTTP_201_CREATED

    return response


@router.get("/posts/{post_id}", response_model=OnePostSchema)
async def get_post(
    response: Response,
    post_id: int,
    session: AsyncSession = Depends(get_async_session),
) -> OnePostSchema:
    post = await get_post_by_id(post_id, session)

    return post
