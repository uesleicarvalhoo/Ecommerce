from datetime import date
from typing import Optional

from factory import Factory, Faker, Sequence, SubFactory

from backend.helpers.constants import PaymentStatus
from backend.infrastructure.schemas.payment import (
    AddressSchema,
    CreditCardSchema,
    CustomerDataSchema,
    PaymentInfoSchema,
    PaymentResultSchema,
)


class PaymentResultSchemaFactory(Factory):
    transaction_id: str = Sequence(lambda i: i)
    status: PaymentStatus = PaymentStatus.SUCCESS
    message: str = "Sucesso!"

    class Meta:
        model = PaymentResultSchema


class CreditCardSchemaFactory(Factory):
    number: int = Faker("credit_card_number")
    security_code: int = Faker("credit_card_security_code")
    due_date: str = Faker("credit_card_expire")

    class Meta:
        model = CreditCardSchema


class AddressSchemaFactory(Factory):
    neighborhood: str = Faker("bairro", locale="pt-br")
    post_code: str = Faker("postcode", locale="pt-br")
    address: str = Faker("address", locale="pt-br")
    complement: Optional[str] = ""

    class Meta:
        model = AddressSchema


class CustomerDataSchemaFactory(Factory):
    document: str = Faker("cpf", locale="pt-br")
    name: str = Faker("name", locale="pt-br")
    birth_date: date = Faker("date")

    class Meta:
        model = CustomerDataSchema


class PaymentInfoSchemaFactory(Factory):
    credit_card: CreditCardSchema = SubFactory(CreditCardSchemaFactory)
    client: CustomerDataSchema = SubFactory(CustomerDataSchemaFactory)
    adress: AddressSchema = SubFactory(AddressSchemaFactory)
    value: float = Faker("pyfloat", positive=True)
    customer: CustomerDataSchema = SubFactory(CustomerDataSchemaFactory)

    class Meta:
        model = PaymentInfoSchema
