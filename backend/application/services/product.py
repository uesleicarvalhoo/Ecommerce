from typing import List
from uuid import UUID

from backend.application.contracts import Product, Repository
from backend.application.schemas import NewProductSchema, ProductSchema, QueryProductSchema


class ProductService:
    def __init__(self, repository: Repository[Product, QueryProductSchema]) -> None:
        self.repository = repository

    def get_by_id(self, id: UUID) -> Product:
        return self.repository.select_one(QueryProductSchema(id=id))

    def get_by_code(self, code: str) -> Product:
        return self.repository.select_one(QueryProductSchema(code=code))

    def get_by_name(self, name: str) -> Product:
        return self.repository.select_one(QueryProductSchema(name=name))

    def get_by_avaliability(self, avaliable: bool) -> List[Product]:
        return self.repository.select_all(QueryProductSchema(avaliable=avaliable))

    def create(self, data: NewProductSchema, storage_key: str) -> Product:
        return ProductSchema(code=data.code, name=data.name, value=data.value, amount=data.amount, file_key=storage_key)

    def save(self, product: Product) -> Product:
        return self.repository.save(product)
