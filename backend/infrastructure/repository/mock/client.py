from backend.infrastructure.contracts import QueryClient
from backend.infrastructure.schemas import ClientSchema


class MockClientRepository:
    def select_one(self, query: QueryClient) -> ClientSchema:
        return None

    def select_all(self, query: QueryClient) -> ClientSchema:
        return []

    def save(self, entity: ClientSchema) -> ClientSchema:
        return entity
