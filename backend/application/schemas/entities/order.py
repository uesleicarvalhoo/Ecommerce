from datetime import datetime
from typing import List, Optional
from uuid import UUID, uuid4

from pydantic import BaseModel, Field

from backend.helpers.constants import OrderStatus
from backend.helpers.date import get_now_datetime

from .client import ClientSchema
from .payment import PaymentResultSchema


class OrderItemSchema(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    name: str
    value: float
    amount: int


class OrderSchema(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    client_id: UUID
    payment_id: str
    date: datetime = Field(default_factory=get_now_datetime)
    description: Optional[str]
    status: OrderStatus
    items: List[OrderItemSchema]

    client: ClientSchema
    payment: PaymentResultSchema
