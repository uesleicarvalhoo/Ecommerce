import pytest
from pytest_mock import MockerFixture

from backend.domain.contracts import EmailService, OrderService, ProductService
from backend.domain.rules.order import CancelOrder
from backend.helpers.constants import OrderStatus
from tests.factories import OrderItemSchemaFactory, OrderSchemaFactory, ProductSchemaFactory


@pytest.fixture()
def sut(
    order_service: OrderService,
    product_service: ProductService,
    email_service: EmailService,
) -> CancelOrder:
    return CancelOrder(order_service=order_service, product_service=product_service, email_service=email_service)


def test_handle_update_item_amount(sut: CancelOrder, mocker: MockerFixture):
    # Arrange
    product = ProductSchemaFactory(amount=10)
    item = OrderItemSchemaFactory(id=product.id, amount=3)
    order = OrderSchemaFactory(items=[item])

    spy = sut.update_product_amount.handle = mocker.Mock()
    sut.order_service.get_by_id = mocker.Mock(return_value=order)
    sut.order_service.product_repository.select_one = mocker.Mock(return_value=product)

    # Action
    sut.handle(order.id)

    # Assert
    expected_updated_amount = 3
    [order_item_id, update_amount], _ = spy.call_args
    assert order_item_id == product.id
    assert update_amount == expected_updated_amount


def test_handle_set_order_status_canceled(sut: CancelOrder, mocker: MockerFixture):
    # Arrange
    product = ProductSchemaFactory(amount=10)
    item = OrderItemSchemaFactory(id=product.id, amount=3)
    order = OrderSchemaFactory(items=[item])

    sut.order_service.get_by_id = mocker.Mock(return_value=order)
    sut.order_service.product_repository.select_one = mocker.Mock(return_value=product)

    # Action
    sut.handle(order.id)

    # Assert
    assert order.status == OrderStatus.CANCELED


def test_handle_save_order_with_status_canceled(sut: CancelOrder, mocker: MockerFixture):
    # Arrange
    product = ProductSchemaFactory(amount=10)
    item = OrderItemSchemaFactory(id=product.id, amount=3)
    order = OrderSchemaFactory(items=[item])

    sut.order_service.get_by_id = mocker.Mock(return_value=order)
    sut.order_service.product_repository.select_one = mocker.Mock(return_value=product)
    spy = sut.order_service.save = mocker.Mock(side_effect=lambda o: o)

    # Action
    sut.handle(order.id)

    # Assert
    assert order.status == OrderStatus.CANCELED
    spy.assert_called_with(order)
