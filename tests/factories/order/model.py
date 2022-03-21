from typing import List
from uuid import UUID, uuid4

from factory import Factory, Faker, LazyFunction
from factory import List as ListSubFactory
from factory import SubFactory

from backend.helpers.constants import OrderStatus
from backend.infrastructure.schemas import ClientSchema, OrderItemSchema, OrderSchema, PaymentResultSchema
from tests.factories.client import ClientSchemaFactory
from tests.factories.payment import PaymentResultSchemaFactory


class OrderItemSchemaFactory(Factory):
    id: UUID = LazyFunction(uuid4)
    name: str = Faker("name", locale="pt-br")
    value: float = Faker("pyfloat", positive=True)
    amount: int = Faker("pyint")

    class Meta:
        model = OrderItemSchema


class OrderSchemaFactory(Factory):
    id: UUID = LazyFunction(uuid4)
    client_id: UUID = LazyFunction(uuid4)
    payment_id: str = LazyFunction(lambda: str(uuid4))
    description: str = Faker("word")
    status = OrderStatus = OrderStatus.COMPLETED
    items: List[OrderItemSchema] = ListSubFactory([SubFactory(OrderItemSchemaFactory)])

    client: ClientSchema = SubFactory(ClientSchemaFactory)
    payment: PaymentResultSchema = SubFactory(PaymentResultSchemaFactory)

    class Meta:
        model = OrderSchema
