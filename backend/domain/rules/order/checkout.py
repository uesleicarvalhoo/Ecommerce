from backend.domain.contracts import (
    Client,
    EmailService,
    NewOrder,
    Order,
    OrderService,
    PaymentInfo,
    PaymentService,
    ProductService,
)
from backend.domain.exceptions import CheckoutError, PaymentRefusedError
from backend.domain.rules.payment import MakeTransaction
from backend.domain.rules.product import CheckProductAvaliability, UpdateProductAmount
from backend.helpers.constants import OrderStatus, PaymentStatus


class OrderCheckout:
    def __init__(
        self,
        order_service: OrderService,
        product_service: ProductService,
        email_service: EmailService,
        payment_service: PaymentService,
    ) -> None:
        self.order_service = order_service
        self.email_service = email_service
        self.check_product_avaliability = CheckProductAvaliability(product_service)
        self.make_transaction = MakeTransaction(payment_service)
        self.update_product_amount = UpdateProductAmount(product_service)

    def handle(self, client: Client, new_order: NewOrder, payment_info: PaymentInfo) -> Order:
        if not new_order.items:
            raise CheckoutError("É necessário ter pelo menos 1 item para finalizar a compra")

        for item in new_order.items:
            self.check_product_avaliability.handle(item.id, item.amount)

        payment_result = self.make_transaction.handle(payment_info)
        order_status = (
            OrderStatus.COMPLETED
            if payment_result.status == PaymentStatus.SUCCESS
            else OrderStatus.CANCELED
            if PaymentStatus.REFUSED
            else OrderStatus.PENDING
        )

        order = self.order_service.create(
            client=client,
            items=new_order.items,
            description=new_order.description,
            status=order_status,
            payment=payment_result,
        )

        if order.payment.status == PaymentStatus.REFUSED:
            self.order_service.save(order)
            raise PaymentRefusedError(
                f"Não foi possível processar a ordem de compra, pagamento recusado, detalhes: {payment_result.message}"
            )

        for item in order.items:
            self.update_product_amount.handle(item.id, -item.amount)

        if payment_result.status == PaymentStatus.SUCCESS:
            order.status = OrderStatus.COMPLETED

        self.order_service.save(order)
        self.email_service.send_new_order_email(client, order)

        return order
