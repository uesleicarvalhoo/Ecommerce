from typing import Protocol

from backend.domain.contracts import PaymentInfo, PaymentResult


class PaymentService(Protocol):
    def make_transaction(self, payment_info: PaymentInfo) -> PaymentResult:
        ...  # pragma: no cover
