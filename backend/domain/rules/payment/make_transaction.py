from backend.domain.contracts import PaymentInfo, PaymentResult, PaymentService


class MakeTransaction:
    def __init__(self, payment_service: PaymentService) -> None:
        self.service = payment_service

    def handle(self, payment_info: PaymentInfo) -> PaymentResult:
        return self.service.make_transaction(payment_info)
