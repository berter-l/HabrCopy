from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from app.api.comments import router as comments_router
from app.api.authentication import router as authentication_router
from app.api.posts import router as posts_router
from app.models.database import async_engine, Base
from templates import all_posts, main_page, one_post_page
from app.api.text_summarizer import router as text_summarizer_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield


app = FastAPI(lifespan=lifespan)


@app.get("/")
async def get_root_html():
    return HTMLResponse(content=main_page.html_main_page)


@app.get("/page/posts/html")
async def get_posts_html():
    return HTMLResponse(content=all_posts.posts_html)


@app.get("/page/posts/{post_id}")
async def get_post_html():
    return HTMLResponse(content=one_post_page.one_post_html)


app.include_router(authentication_router)
app.include_router(posts_router)
app.include_router(comments_router)
app.include_router(text_summarizer_router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
