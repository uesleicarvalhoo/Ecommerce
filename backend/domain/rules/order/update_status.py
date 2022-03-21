from uuid import UUID

from backend.domain.contracts import Order, OrderService
from backend.helpers.constants import OrderStatus


class UpdateOrderStatus:
    def __init__(self, service: OrderService) -> None:
        self.service = service

    def handle(self, order_id: UUID, new_status: OrderStatus) -> Order:
        order = self.service.get_by_id(order_id)
        order.status = new_status
        return self.service.save(order)
