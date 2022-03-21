from typing import Protocol
from uuid import UUID


class Product(Protocol):
    id: UUID
    code: str
    name: str
    value: float
    amount: int
    file_key: str
