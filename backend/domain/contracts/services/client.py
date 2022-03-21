from typing import List, Protocol
from uuid import UUID

from backend.domain.contracts.entities import Client
from backend.domain.contracts.schemas import NewClient


class ClientService(Protocol):
    def get_all(self) -> List[Client]:
        ...  # pragma: no cover

    def get_by_id(self, id: UUID) -> Client:
        ...  # pragma: no cover

    def get_by_email(self, email: str) -> Client:
        ...  # pragma: no cover

    def get_by_phone(self, phone: str) -> Client:
        ...  # pragma: no cover

    def create(self, data: NewClient) -> Client:
        ...  # pragma: no cover

    def save(self, entity: Client) -> Client:
        ...  # pragma: no cover
