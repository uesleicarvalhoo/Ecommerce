from uuid import UUID

from backend.domain.contracts import ProductService
from backend.domain.exceptions import ProductUnavaliableError


class CheckProductAvaliability:
    def __init__(self, service: ProductService) -> None:
        self.service = service

    def handle(self, product_id: UUID, amount: int) -> None:
        product = self.service.get_by_id(product_id)
        if not product.amount >= amount:
            raise ProductUnavaliableError(
                f"Produto {product.name} não possui estoque suficiente, estoque atual: {product.amount}"
            )
