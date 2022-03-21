from uuid import uuid4

from backend.helpers.constants import PaymentStatus
from backend.infrastructure.contracts import PaymentInfo
from backend.infrastructure.schemas import PaymentResultSchema


class FakePaymentController:
    def make_credit_card_payment(self, payment_info: PaymentInfo) -> PaymentResultSchema:
        return PaymentResultSchema(transaction_id=str(uuid4()), status=PaymentStatus.SUCCESS)
