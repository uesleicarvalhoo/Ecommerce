from typing import Protocol
from uuid import UUID


class Client(Protocol):
    id: UUID
    name: str
    email: str
    phone: str
    password_hash: str
