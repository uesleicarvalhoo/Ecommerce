import pytest
from pytest_mock import MockerFixture

from backend.domain.contracts import EmailService, OrderService, PaymentService, ProductService
from backend.domain.exceptions import CheckoutError, PaymentRefusedError
from backend.domain.rules.order import OrderCheckout
from backend.helpers.constants import PaymentStatus
from tests.factories import (
    ClientSchemaFactory,
    NewOrderFactory,
    NewOrderItemFactory,
    PaymentInfoSchemaFactory,
    PaymentResultSchemaFactory,
    ProductSchemaFactory,
)


@pytest.fixture()
def sut(
    order_service: OrderService,
    product_service: ProductService,
    email_service: EmailService,
    payment_service: PaymentService,
) -> OrderCheckout:
    return OrderCheckout(
        order_service=order_service,
        product_service=product_service,
        email_service=email_service,
        payment_service=payment_service,
    )


def test_handle_when_new_order_items_is_empty_then_raise_checkout_error(sut: OrderCheckout):
    # Arrange
    order = NewOrderFactory(items=[])
    client = ClientSchemaFactory()
    payment = PaymentInfoSchemaFactory()

    # Action/Assert
    with pytest.raises(CheckoutError):
        sut.handle(client, order, payment)


def test_handle_call_update_products_amount(sut: OrderCheckout, mocker: MockerFixture):
    # Arrange
    client = ClientSchemaFactory()
    payment = PaymentInfoSchemaFactory()
    product = ProductSchemaFactory(amount=10)
    item = NewOrderItemFactory(id=product.id, amount=3)
    order = NewOrderFactory(items=[item])

    spy = sut.update_product_amount.handle = mocker.Mock()
    sut.order_service.product_repository.select_one = mocker.Mock(return_value=product)

    # Action
    sut.handle(client, order, payment)

    # Assert
    expected_updated_amount = -3
    [order_item_id, update_amount], _ = spy.call_args
    assert order_item_id == product.id
    assert update_amount == expected_updated_amount


def test_handle_when_payment_is_refused_then_raise_payment_error_exception(sut: OrderCheckout, mocker: MockerFixture):
    # Arrange
    client = ClientSchemaFactory()
    payment = PaymentInfoSchemaFactory()
    product = ProductSchemaFactory(amount=10)
    item = NewOrderItemFactory(id=product.id, amount=3)
    order = NewOrderFactory(items=[item])

    sut.order_service.product_repository.select_one = mocker.Mock(return_value=product)
    sut.make_transaction.handle = mocker.Mock(return_value=PaymentResultSchemaFactory(status=PaymentStatus.REFUSED))

    # Action/Assert
    with pytest.raises(PaymentRefusedError):
        sut.handle(client, order, payment)
