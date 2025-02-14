from fastapi import WebSocket, WebSocketDisconnect, APIRouter
from typing import List

router = APIRouter()
active_connections: List[WebSocket] = []

@router.websocket("/ws/{client_id}")
async def websocket_endpoint(websocket: WebSocket, client_id: int):
    await websocket.accept()
    active_connections.append(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            for connection in active_connections:
                await connection.send_text(f"Client {client_id}: {data}")
    except WebSocketDisconnect:
        active_connections.remove(websocket)
