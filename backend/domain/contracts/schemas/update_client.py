from typing import Protocol


class UpdateClientData(Protocol):
    name: str = None
    email: str = None
    phone: str = None
