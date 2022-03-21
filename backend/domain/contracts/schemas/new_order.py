from typing import List, Protocol
from uuid import UUID


class NewOrderItem(Protocol):
    id: UUID
    amount: int


class NewOrder(Protocol):
    client_id: UUID
    items: List[NewOrderItem]
    amount: int
