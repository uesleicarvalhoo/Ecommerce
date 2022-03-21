from typing import List
from uuid import UUID

from backend.application.contracts import Client, Repository
from backend.application.schemas import ClientSchema, NewClientSchema, QueryClientSchema

from .auth import AuthenticationService


class ClientService:
    def __init__(
        self, repository: Repository[Client, QueryClientSchema], authentication_service: AuthenticationService
    ) -> None:
        self.repository = repository
        self.auth_service = authentication_service

    def get_all(self) -> List[Client]:
        return self.repository.select_all(QueryClientSchema())

    def get_by_id(self, id: UUID) -> Client:
        return self.repository.select_one(QueryClientSchema(id=id))

    def get_by_email(self, email: str) -> Client:
        return self.repository.select_one(QueryClientSchema(email=email))

    def get_by_phone(self, phone: str) -> Client:
        return self.repository.select_one(QueryClientSchema(phone=phone))

    def create(self, data: NewClientSchema) -> Client:
        return ClientSchema(
            name=data.name,
            email=data.email,
            phone=data.phone,
            password_hash=self.auth_service.generate_password_hash(data.password),
        )

    def save(self, client: Client) -> Client:
        return self.repository.save(client)
