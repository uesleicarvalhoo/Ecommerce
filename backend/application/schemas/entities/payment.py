from datetime import date
from typing import Optional

from pydantic import BaseModel

from backend.helpers.constants import PaymentStatus


class PaymentResultSchema(BaseModel):
    transaction_id: str
    status: PaymentStatus
    message: Optional[str]


class CustomerDataSchema(BaseModel):
    name: str
    document: str
    birth_date: date


class CreditCardSchema(BaseModel):
    number: int
    security_code: int
    due_date: str


class AddressSchema(BaseModel):
    neighborhood: str
    post_code: str
    address: str
    complement: Optional[str]


class PaymentInfoSchema(BaseModel):
    customer: CustomerDataSchema
    credit_card: CreditCardSchema
    adress: AddressSchema
    value: float
