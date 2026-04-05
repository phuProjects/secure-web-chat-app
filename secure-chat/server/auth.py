"""
Password hashing and verification (bcrypt).
Phase 2+: implement hash_password and verify_password.
"""

from __future__ import annotations


def hash_password(plain: str) -> str:
    raise NotImplementedError("Phase 2: bcrypt hash")


def verify_password(plain: str, hashed: str) -> bool:
    raise NotImplementedError("Phase 2: bcrypt verify")
