from typing import List
from uuid import UUID, uuid4

from factory import Factory, Faker, LazyFunction
from factory import List as ListFactory
from factory import SubFactory

from backend.domain.schemas import NewOrderItemSchema, NewOrderSchema
from backend.helpers.constants import SaleType


class NewOrderItemFactory(Factory):
    id: UUID = LazyFunction(uuid4)
    amount: int = Faker("pyint")

    class Meta:
        model = NewOrderItemSchema


class NewOrderFactory(Factory):
    items: List[NewOrderItemSchema] = ListFactory([SubFactory(NewOrderItemFactory)])
    description: str = Faker("word")
    amount: int = Faker("pyint")
    sale_type = SaleType.SALE_IN_DEBT

    class Meta:
        model = NewOrderSchema
