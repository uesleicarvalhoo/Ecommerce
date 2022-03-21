from typing import List, Protocol
from uuid import UUID

from backend.domain.contracts import Client, Order, OrderItem, PaymentResult
from backend.helpers.constants import OrderStatus


class OrderService(Protocol):
    def get_by_id(self, id: UUID) -> Order:
        ...  # pragma: no cover

    def create(
        self, client: Client, items: List[OrderItem], description: str, status: OrderStatus, payment: PaymentResult
    ) -> Order:
        ...  # pragma: no cover

    def save(self, data: Order) -> Order:
        ...  # pragma: no cover
