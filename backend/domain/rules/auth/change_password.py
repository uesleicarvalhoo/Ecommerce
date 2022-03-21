from uuid import UUID

from backend.domain.contracts import AuthenticationService, Client, ClientService


class ChangePassword:
    def __init__(self, service: ClientService, authentication: AuthenticationService) -> None:
        self.service = service
        self.auth = authentication

    def handle(self, client_id: UUID, new_password: str) -> Client:
        client = self.service.get_by_id(client_id)

        client.password_hash = self.auth.generate_password_hash(new_password)

        self.service.save(client)

        return client
