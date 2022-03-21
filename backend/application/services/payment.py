from backend.application.contracts import PaymentController, PaymentInfo, PaymentResult


class PaymentService:
    def __init__(self, controller: PaymentController):
        self.controller = controller

    def make_transaction(self, payment_info: PaymentInfo) -> PaymentResult:
        return self.controller.make_credit_card_payment(payment_info)
