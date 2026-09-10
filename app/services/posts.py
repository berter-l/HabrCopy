from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from app.models.posts import Posts
from app.schemes.posts import ResponseManyPostsSchema


async def get_processed_posts(raw_posts):
    posts_title = [post.title for post in raw_posts]
    posts_id = [post.id for post in raw_posts]

    return ResponseManyPostsSchema(title=posts_title, id=posts_id)


async def get_all_posts_title(session: AsyncSession):
    posts_query = select(Posts)

    raw_posts = await session.scalars(posts_query)
    raw_posts = raw_posts.all()

    posts_title = await get_processed_posts(raw_posts)
    return posts_title


async def get_post_by_id(post_id: int, session: AsyncSession):
    post_query = (
        select(Posts).filter_by(id=post_id).options(selectinload(Posts.comments))
    )

    post = await session.scalar(post_query)

    if post is None:
        raise HTTPException(status_code=404, detail="Post not found")

    return post


async def create_post(title: str, content: str, user_id: int, session: AsyncSession):
    post = Posts(title=title, content=content, user_id=user_id)

    session.add(post)

    await session.commit()


async def delete_post_by_id(post_id: int, session: AsyncSession):
    post = await get_post_by_id(post_id, session)

    await session.delete(post)
