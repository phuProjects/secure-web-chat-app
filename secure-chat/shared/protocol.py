"""
Wire message types and helpers for WebSocket JSON payloads.
Keep in sync with client/app.js message type strings.
"""

from __future__ import annotations

import json
from typing import Any

# --- Message types (Phase 1+) ---
MSG_CHAT = "chat"
MSG_REGISTER = "register"
MSG_LOGIN = "login"
MSG_ERROR = "error"
MSG_UPLOAD_PUBLIC_KEY = "upload_public_key"
MSG_GET_PUBLIC_KEY = "get_public_key"
MSG_SECURE_CHAT = "secure_chat"


def parse_message(raw: str) -> dict[str, Any]:
    """Parse incoming WebSocket text as JSON object."""
    data = json.loads(raw)
    if not isinstance(data, dict):
        raise ValueError("message must be a JSON object")
    return data


def encode_json(obj: dict[str, Any]) -> str:
    return json.dumps(obj)
