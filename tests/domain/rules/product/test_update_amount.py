import pytest
from pytest_mock import MockerFixture

from backend.domain.contracts import ProductService
from backend.domain.rules.product.update_amount import UpdateProductAmount
from tests.factories import ProductSchemaFactory


@pytest.fixture()
def sut(product_service: ProductService) -> UpdateProductAmount:
    return UpdateProductAmount(product_service)


def test_handle_when_new_amount_is_lower_then_0_then_raise_value_error(sut: UpdateProductAmount, mocker: MockerFixture):
    # Arrange
    product = ProductSchemaFactory()
    sut.service.get_by_id = mocker.Mock(return_value=product)
    update_amount = -product.amount - 1

    # Action/Assert
    with pytest.raises(ValueError):
        sut.handle(product.id, update_amount)


def test_handle_when_amount_is_greater_then_0_then_product_amount_is_incremented(
    sut: UpdateProductAmount, mocker: MockerFixture
):
    # Arrange
    product = ProductSchemaFactory(amount=10)
    sut.service.get_by_id = mocker.Mock(return_value=product)
    update_amount = 5
    expected_new_amount = 15

    # Action
    sut.handle(product.id, update_amount)

    # Assert
    assert product.amount == expected_new_amount


def test_handle_when_amount_is_lower_then_0_then_product_amount_is_decremented(
    sut: UpdateProductAmount, mocker: MockerFixture
):
    # Arrange
    product = ProductSchemaFactory(amount=10)
    sut.service.get_by_id = mocker.Mock(return_value=product)
    update_amount = -5
    expected_new_amount = 5

    # Action
    sut.handle(product.id, update_amount)

    # Assert
    assert product.amount == expected_new_amount
