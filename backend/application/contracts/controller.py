from typing import Protocol

from backend.application.contracts import Order, PaymentInfo, PaymentResult


class PaymentController(Protocol):
    def make_credit_card_payment(self, payment_info: PaymentInfo, order: Order) -> PaymentResult:
        ...  # pragma: no cover
