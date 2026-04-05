"""
WebSocket chat server entrypoint.
Phase 1+: accept connections, route messages; import storage/auth as phases land.
"""

from __future__ import annotations

import asyncio
import logging
import sys
from pathlib import Path

# Allow `python server/server.py` and imports of shared/
_ROOT = Path(__file__).resolve().parents[1]
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))

import websockets

from shared.protocol import MSG_CHAT, encode_json, parse_message

logging.basicConfig(
    level=logging.INFO,
    format="[%(levelname)s] %(message)s",
)
log = logging.getLogger(__name__)

# Connected clients (Phase 1: in-memory set)
CLIENTS: set = set()


async def handler(websocket):
    CLIENTS.add(websocket)
    log.info("Client connected (%s)", len(CLIENTS))
    try:
        async for raw in websocket:
            try:
                msg = parse_message(raw)
                mtype = msg.get("type")
                if mtype == MSG_CHAT:
                    text = msg.get("text", "")
                    out = encode_json({"type": MSG_CHAT, "text": text})
                    for ws in list(CLIENTS):
                        try:
                            await ws.send(out)
                        except Exception:
                            pass
                else:
                    log.debug("Unhandled type: %s", mtype)
            except Exception as exc:
                log.warning("Bad message: %s", exc)
    finally:
        CLIENTS.discard(websocket)
        log.info("Client disconnected (%s)", len(CLIENTS))


async def main():
    host = "127.0.0.1"
    port = 8765
    async with websockets.serve(handler, host, port):
        log.info("WebSocket server ws://%s:%s", host, port)
        await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(main())
