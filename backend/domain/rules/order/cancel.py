from uuid import UUID

from backend.domain.contracts import EmailService, Order, OrderService, ProductService
from backend.domain.rules.product.update_amount import UpdateProductAmount
from backend.helpers.constants import OrderStatus


class CancelOrder:
    def __init__(
        self, order_service: OrderService, product_service: ProductService, email_service: EmailService
    ) -> None:
        self.order_service = order_service
        self.email_service = email_service
        self.update_product_amount = UpdateProductAmount(product_service)

    def handle(self, order_id: UUID) -> Order:
        order = self.order_service.get_by_id(order_id)
        order.status = OrderStatus.CANCELED

        for item in order.items:
            self.update_product_amount.handle(item.id, item.amount)

        self.order_service.save(order)
        self.email_service.send_new_order_email(order.client, order)

        return order
