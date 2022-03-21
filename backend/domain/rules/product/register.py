from uuid import uuid4

from backend.domain.contracts import NewProduct, Product, ProductService, Storage
from backend.domain.exceptions import DuplicatedDataError, NotFoundError


class RegisterProduct:
    def __init__(self, service: ProductService, storage: Storage):
        self.service = service
        self.storage = storage

    def _check_if_product_code_already_used(self, code: str) -> bool:
        try:
            self.service.get_by_code(code)
        except NotFoundError:
            return False
        else:
            return True

    def _check_if_product_name_already_used(self, name: str) -> bool:
        try:
            self.service.get_by_name(name)
        except NotFoundError:
            return False
        else:
            return True

    def handle(self, data: NewProduct, binary: bytes) -> Product:
        if self._check_if_product_code_already_used(data.code):
            raise DuplicatedDataError(f"Já existe um produto cadastrado com o código {data.code}")

        if self._check_if_product_name_already_used(data.name):
            raise DuplicatedDataError(f"Já existe um produto com o nome {data.name}")

        key = self.storage.upload(f"product-{uuid4()}", binary)
        return self.service.create(data, key)
