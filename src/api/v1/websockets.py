"""WebSocket Manager for Real-Time Inundation Depth Broadcasts."""

import json
from typing import Dict, List, Set
from fastapi import APIRouter, WebSocket, WebSocketDisconnect

from src.config import settings

router = APIRouter(tags=["WebSockets"])


class InundationConnectionManager:
    """Manages active WebSocket connections with client concurrency caps."""

    def __init__(self, max_connections: int = settings.MAX_WS_CONNECTIONS):
        self.active_connections: Set[WebSocket] = set()
        self.max_connections = max_connections

    async def connect(self, websocket: WebSocket) -> bool:
        """Accepts new WebSocket client if below connection threshold."""
        if len(self.active_connections) >= self.max_connections:
            await websocket.close(code=1008, reason="Max WebSocket connections reached.")
            return False

        await websocket.accept()
        self.active_connections.add(websocket)
        return True

    def disconnect(self, websocket: WebSocket) -> None:
        """Removes a disconnected client."""
        self.active_connections.discard(websocket)

    async def broadcast_inundation_update(self, message: dict) -> None:
        """Broadcasts live flood depth updates to all active dashboard/GIS subscribers."""
        dead_connections = []
        payload = json.dumps(message)

        for connection in list(self.active_connections):
            try:
                await connection.send_text(payload)
            except Exception:
                dead_connections.append(connection)

        for conn in dead_connections:
            self.active_connections.discard(conn)


ws_manager = InundationConnectionManager()


@router.websocket("/ws/inundation")
async def websocket_inundation_feed(websocket: WebSocket):
    """Real-time streaming WebSocket endpoint for GIS and Emergency Response maps."""
    connected = await ws_manager.connect(websocket)
    if not connected:
        return

    try:
        # Send initial confirmation handshake
        await websocket.send_json({
            "type": "connection_established",
            "message": "Connected to Urban Flood Inundation Stream",
            "subscribed_horizons": settings.NOWCAST_HORIZONS_MINUTES,
        })

        while True:
            # Keep connection alive and listen for client filter requests
            data = await websocket.receive_text()
            # Client can send ping or custom threshold filters
            try:
                parsed = json.loads(data)
                if parsed.get("action") == "ping":
                    await websocket.send_json({"type": "pong"})
            except Exception:
                pass
    except WebSocketDisconnect:
        ws_manager.disconnect(websocket)
    except Exception:
        ws_manager.disconnect(websocket)
