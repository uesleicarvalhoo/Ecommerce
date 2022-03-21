from typing import List, Protocol
from uuid import UUID

from backend.domain.contracts.entities import Product
from backend.domain.contracts.schemas import NewProduct


class ProductService(Protocol):
    def get_by_id(self, id: UUID) -> Product:
        ...  # pragma: no cover

    def get_by_code(self, code: str) -> Product:
        ...  # pragma: no cover

    def get_by_name(self, name: str) -> Product:
        ...  # pragma: no cover

    def get_by_avaliability(self, avaliable: bool) -> List[Product]:
        ...  # pragma: no cover

    def save(self, product: Product) -> Product:
        ...  # pragma: no cover

    def create(self, data: NewProduct, storage_key: str) -> Product:
        ...  # pragma: no cover
