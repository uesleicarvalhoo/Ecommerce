from typing import List

from backend.infrastructure.contracts import QueryProduct
from backend.infrastructure.schemas import ProductSchema


class MockProductRepository:
    def select_one(self, query: QueryProduct) -> ProductSchema:
        return None

    def select_all(self, query: QueryProduct) -> List[ProductSchema]:
        return []

    def save(self, entity: ProductSchema) -> ProductSchema:
        return entity
