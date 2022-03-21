from datetime import date
from typing import Optional, Protocol

from backend.helpers.constants import PaymentStatus


class PaymentResult(Protocol):
    transaction_id: str
    status: PaymentStatus
    message: Optional[str]


class CustomerData(Protocol):
    name: str
    document: str
    birth_date: date


class CreditCard(Protocol):
    number: int
    security_code: int
    due_date: str
    holder: CustomerData


class Address(Protocol):
    neighborhood: str
    post_code: str
    address: str
    complement: Optional[str]


class PaymentInfo(Protocol):
    credit_card: CreditCard
    client: CustomerData
    adress: Address
    value: float
