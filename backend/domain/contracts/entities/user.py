from typing import Protocol
from uuid import UUID


class User(Protocol):
    id: UUID
    email: str
    password_hash: str
