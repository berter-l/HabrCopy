from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.services.text_summarize import get_post_summary as service_get_post_summary
from app.dependencies import get_async_session

router = APIRouter()


@router.get("/ai/summarize/{post_id}/")
async def get_summarize_text(
    post_id: int, session: AsyncSession = Depends(get_async_session)
):
    summarized_text = await service_get_post_summary(post_id, session)
    return summarized_text
