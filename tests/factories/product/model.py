from uuid import UUID, uuid4

from factory import Factory, Faker, LazyAttribute, LazyFunction

from backend.infrastructure.schemas import ProductSchema


class ProductSchemaFactory(Factory):
    id: UUID = LazyFunction(uuid4)
    code: str = Faker("pystr", max_chars=5)
    name: str = Faker("word", locale="pt-br")
    value: float = Faker("pyfloat", positive=True)
    amount: int = Faker("pyint")
    file_key: str = LazyAttribute(lambda o: f"product-{o.id}")

    class Meta:
        model = ProductSchema
