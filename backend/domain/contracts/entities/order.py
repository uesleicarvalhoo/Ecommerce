from datetime import datetime
from typing import List, Optional, Protocol
from uuid import UUID

from backend.helpers.constants import OrderStatus

from .client import Client
from .payment import PaymentResult


class OrderItem(Protocol):
    id: UUID
    name: str
    value: float
    amount: int


class Order(Protocol):
    id: UUID
    client: Client
    payment: Optional[PaymentResult]
    date: datetime
    description: Optional[str]
    status: OrderStatus
    items: List[OrderItem]
