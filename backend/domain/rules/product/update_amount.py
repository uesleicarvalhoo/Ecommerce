from uuid import UUID

from backend.domain.contracts import Product, ProductService


class UpdateProductAmount:
    def __init__(self, service: ProductService) -> None:
        self.service = service

    def handle(self, product_id: UUID, quantity: int) -> Product:
        product = self.service.get_by_id(product_id)
        new_amount = product.amount + quantity

        if new_amount < 0:
            raise ValueError(f"Estoque insuficiente para o produto {product.name}")

        product.amount = new_amount
        return self.service.save(product)
