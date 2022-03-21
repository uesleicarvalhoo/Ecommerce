from random import randint
from uuid import UUID, uuid4

from factory import Factory, Faker, LazyAttribute, LazyFunction

from backend.infrastructure.schemas import ClientSchema


class ClientSchemaFactory(Factory):
    id: UUID = LazyFunction(uuid4)
    name: str = Faker("name", locale="pt-br")
    email: str = LazyAttribute(lambda o: f"{o.name.replace(' ', '.')}@email.com")
    phone: str = LazyFunction(lambda: f"{randint(11, 99)}9{randint(80000000, 99999999)}")
    password_hash: str = Faker("pystr")

    class Meta:
        model = ClientSchema
