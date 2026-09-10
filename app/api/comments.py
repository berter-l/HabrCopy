from fastapi import WebSocket, APIRouter, Depends
from starlette.websockets import WebSocketDisconnect

from app.websocket_connect_manager import ConnectManager
from app.dependencies import get_ws_user_id

router = APIRouter()

manager = ConnectManager()


@router.websocket("/posts/ws/{post_id}/")
async def websocket_endpoint(
    websocket: WebSocket, post_id: int, user_id: int = Depends(get_ws_user_id)
):
    await manager.connect(websocket, post_id=post_id)
    try:
        while True:
            raw_message = await websocket.receive()

            if raw_message["type"] == "websocket.disconnect":
                raise WebSocketDisconnect()

            message_type = "text" if "text" in raw_message else "bytes"

            message_content = raw_message[message_type]

            await manager.send_comment(
                message_content,
                message_type=message_type,
                post_id=post_id,
                user_id=user_id,
            )

    except WebSocketDisconnect:
        await manager.disconnect(websocket, post_id=post_id)
