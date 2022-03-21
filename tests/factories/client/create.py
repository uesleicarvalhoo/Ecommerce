from random import randint

import factory

from backend.domain.schemas import NewClientSchema


class NewClientFactory(factory.Factory):
    name: str = factory.Faker("name", locale="pt-br")
    email: str = factory.LazyAttribute(lambda o: f"{o.name.replace(' ', '.')}@email.com")
    phone: str = factory.LazyFunction(lambda: f"{randint(11, 99)}9{randint(80000000, 99999999)}")
    password: str = factory.Faker("word")
    admin: bool = False

    class Meta:
        model = NewClientSchema
