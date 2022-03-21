from typing import Protocol


class NewClient(Protocol):
    name: str
    email: str
    phone: str
    password: str
