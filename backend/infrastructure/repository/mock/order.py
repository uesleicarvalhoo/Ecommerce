from typing import List

from backend.infrastructure.contracts import QueryOrder
from backend.infrastructure.schemas import OrderSchema


class MockOrderRepository:
    def select_one(self, query: QueryOrder):
        return None

    def select_all(self, query: QueryOrder) -> List[OrderSchema]:
        return []

    def save(self, entity: OrderSchema) -> OrderSchema:
        return entity
