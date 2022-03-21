import pytest
from pytest_mock import MockerFixture

from backend.domain.contracts import ProductService
from backend.domain.exceptions import ProductUnavaliableError
from backend.domain.rules.product import CheckProductAvaliability
from tests.factories import ProductSchemaFactory


@pytest.fixture()
def sut(product_service: ProductService) -> CheckProductAvaliability:
    return CheckProductAvaliability(product_service)


def test_handle_raise_product_unavaliable_error_when_required_amount_is_lower_then_item_amount(
    sut: CheckProductAvaliability, mocker: MockerFixture
):
    # Arrange
    amount = 10
    product = ProductSchemaFactory(amount=amount)
    sut.service.get_by_id = mocker.Mock(return_value=product)

    # Action/Assert
    with pytest.raises(ProductUnavaliableError):
        sut.handle(product.id, amount + 1)


def test_handle_not_raise_error_when_required_amount_is_greater_then_item_amount(
    sut: CheckProductAvaliability, mocker: MockerFixture
):
    # Arrange
    amount = 10
    product = ProductSchemaFactory(amount=amount)
    sut.service.get_by_id = mocker.Mock(return_value=product)

    # Action/Assert
    sut.handle(product.id, amount - 1)


def test_handle_not_raise_error_when_required_amount_is_equal_then_item_amount(
    sut: CheckProductAvaliability, mocker: MockerFixture
):
    # Arrange
    amount = 10
    product = ProductSchemaFactory(amount=amount)
    sut.service.get_by_id = mocker.Mock(return_value=product)

    # Action / Assert
    sut.handle(product.id, amount)
