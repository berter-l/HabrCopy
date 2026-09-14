from collections import defaultdict

from fastapi import WebSocket

from app.config.conf import settings
from app.models import Comments
from app.models.database import async_session
from app.services.comments import upload_file_to_s3
from app.services.comments import build_file_path


class ConnectManager:
    def __init__(self):
        self.connections_users_to_posts = defaultdict(list)

    async def connect(self, websocket: WebSocket, post_id: int):

        await websocket.accept()

        self.connections_users_to_posts[post_id].append(websocket)

    async def disconnect(self, websocket: WebSocket, post_id: int):

        self.connections_users_to_posts[post_id].remove(websocket)

        await websocket.close()

    async def send_comment(
        self, message: str, post_id: int, user_id: int
    ):

        comment_content = await self.save_comment_to_database(message, post_id, user_id)

        for user_connect in self.connections_users_to_posts[post_id]:
            await user_connect.send_text(comment_content)

    async def save_comment_to_database(
        self, message: str | bytes, post_id: int, user_id: int
    ):
        session = async_session()

        comment_content = message

        if isinstance(message, bytes):
            file_path = await build_file_path(post_id)

            await upload_file_to_s3(message, file_path)

            comment_content = f"https://{settings.s3_conf.domain_bucket_name}.s3.cloud.ru/{file_path}"

        try:

            comment = Comments(
                user_id=user_id, post_id=post_id, comment_content=comment_content
            )
            session.add(comment)
            await session.commit()

            return comment_content

        except:
            await session.rollback()
