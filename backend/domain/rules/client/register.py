from backend.domain.contracts import Client, ClientService, NewClient
from backend.domain.exceptions import DuplicatedDataError, NotFoundError


class RegisterClient:
    def __init__(self, service: ClientService) -> None:
        self.service = service

    def _check_if_email_is_already_used(self, email: str) -> bool:
        try:
            self.service.get_by_email(email)
        except NotFoundError:
            return False
        else:
            return True

    def _check_if_phone_is_already_used(self, phone: str) -> bool:
        try:
            self.service.get_by_phone(phone)
        except NotFoundError:
            return False
        else:
            return True

    def handle(self, data: NewClient) -> Client:
        if self._check_if_email_is_already_used(data.email):
            raise DuplicatedDataError(f"Já existe um cliente com o email {data.email} cadastrado")

        if self._check_if_phone_is_already_used(data.phone):
            raise DuplicatedDataError(f"Já existe um cliente com o telefone {data.phone} cadastrado")

        return self.service.create(data)
