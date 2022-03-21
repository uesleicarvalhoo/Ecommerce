from uuid import UUID

from backend.domain.contracts import Client, ClientService, UpdateClientData


class UpdateClient:
    def __init__(self, service: ClientService) -> None:
        self.service = service

    def handle(self, client_id: UUID, data: UpdateClientData) -> Client:
        client = self.service.get_by_id(client_id)

        if data.name is not None:
            client.name = data.name.strip()

        if data.email is not None:
            client.email = data.email

        if data.phone is not None:
            client.phone = data.phone

        return self.service.save(client)
