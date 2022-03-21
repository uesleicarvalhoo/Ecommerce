from factory import Factory, Faker

from backend.domain.schemas import NewProductSchema


class NewProductFactory(Factory):
    code: str = Faker("pystr", max_chars=5)
    name: str = Faker("word", locale="pt-br")
    value: float = Faker("pyfloat", positive=True)
    amount: int = Faker("pyint")

    class Meta:
        model = NewProductSchema
