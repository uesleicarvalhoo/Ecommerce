from uuid import UUID

from backend.domain.contracts import Client, ClientService


class LoadClient:
    def __init__(self, service: ClientService) -> None:
        self.service = service

    def handle(self, client_id: UUID) -> Client:
        return self.service.get_by_id(client_id)
