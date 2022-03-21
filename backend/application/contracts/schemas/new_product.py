from typing import Protocol


class NewProduct(Protocol):
    code: str
    name: str
    value: float
    amount: int
