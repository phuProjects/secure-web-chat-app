"""
SQLite persistence: users (bcrypt hash), public keys.
Phase 2+: implement create_user, get_user_hash, upsert_public_key, get_public_key.
"""

from __future__ import annotations

import sqlite3
from pathlib import Path

# Default DB path relative to server working directory
DEFAULT_DB_PATH = Path(__file__).resolve().parent / "chat.db"


def get_connection(db_path: Path | None = None) -> sqlite3.Connection:
    path = db_path or DEFAULT_DB_PATH
    conn = sqlite3.connect(path)
    conn.row_factory = sqlite3.Row
    return conn


def init_schema(conn: sqlite3.Connection) -> None:
    """Create tables if missing."""
    conn.executescript(
        """
        CREATE TABLE IF NOT EXISTS users (
            username TEXT PRIMARY KEY,
            password_hash TEXT NOT NULL
        );
        CREATE TABLE IF NOT EXISTS public_keys (
            username TEXT PRIMARY KEY,
            public_key_b64 TEXT NOT NULL,
            FOREIGN KEY (username) REFERENCES users(username)
        );
        """
    )
    conn.commit()
