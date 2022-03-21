from backend.domain.contracts import ClientService


class ListAllClients:
    def __init__(self, client_service: ClientService) -> None:
        self.service = client_service

    def handle(self) -> None:
        return self.service.get_all()
