from openai import AsyncOpenAI
from sqlalchemy.ext.asyncio import AsyncSession
from app.config.conf import settings
from app.services.posts import get_post_by_id
from redis.asyncio import Redis as AsyncRedis

REDIS_HOST = settings.redis_conf.server_name

REDIS_PORT = settings.redis_conf.port

AI_BASE_URL = settings.ai_conf.base_url

AI_API_KEY = settings.ai_conf.api_key

ai_client = AsyncOpenAI(api_key=AI_API_KEY, base_url=AI_BASE_URL)

async_redis_client = AsyncRedis(host=REDIS_HOST, port=REDIS_PORT)


async def get_post_summary(post_id: int, session: AsyncSession):
    post = await get_post_by_id(post_id, session)

    summary_text = await get_cached_text(post.id)

    if summary_text is not None:
        return summary_text

    post_content = post.content

    response = await ai_client.chat.completions.create(
        model="gemma2:2b",
        messages=[
            {
                "role": "user",
                "content": f"Сделай краткую выжимку данного текста, нужно только самое главное и пиши на русском: {post_content}",
            }
        ],
        stream=False,
    )
    answer_text = response.choices[0].message.content

    await save_summary_text_to_cache(post.id, answer_text)

    return answer_text


async def get_cached_text(post_id: int):
    summary_text = await async_redis_client.get(f"summary-{post_id}")

    return summary_text


async def save_summary_text_to_cache(post_id: int, summary_text: str):
    await async_redis_client.set(f"summary-{post_id}", summary_text)
    return None
