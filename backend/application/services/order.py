from typing import List
from uuid import UUID

from backend.application.contracts import Client, Order, OrderItem, PaymentResult, Product, Repository
from backend.application.schemas import OrderItemSchema, OrderSchema, QueryOrderSchema, QueryProductSchema
from backend.helpers.constants import OrderStatus


class OrderService:
    def __init__(
        self,
        order_repository: Repository[Order, QueryOrderSchema],
        product_repository: Repository[Product, QueryProductSchema],
    ) -> None:
        self.order_repository = order_repository
        self.product_repository = product_repository

    def get_by_id(self, id: UUID) -> Order:
        return self.order_repository.select_one(QueryOrderSchema(id=id))

    def create_order_item(self, item: OrderItem) -> OrderItemSchema:
        product = self.product_repository.select_one(QueryProductSchema(id=item.id))
        return OrderItemSchema(id=product.id, name=product.name, value=product.value, amount=item.amount)

    def create(
        self, client: Client, items: List[OrderItem], description: str, status: OrderStatus, payment: PaymentResult
    ) -> Order:
        order = OrderSchema(
            client_id=client.id,
            description=description,
            status=status,
            items=[self.create_order_item(item) for item in items],
            payment_id=payment.transaction_id,
            payment=payment,
            client=client,
        )
        return order

    def save(self, data: Order) -> Order:
        return self.order_repository.save(data)
