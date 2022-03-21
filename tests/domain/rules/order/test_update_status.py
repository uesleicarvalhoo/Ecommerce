import pytest
from pytest_mock import MockerFixture

from backend.domain.contracts import OrderService
from backend.domain.rules.order import UpdateOrderStatus
from backend.helpers.constants import OrderStatus
from tests.factories import OrderSchemaFactory


@pytest.fixture()
def sut(
    order_service: OrderService,
) -> UpdateOrderStatus:
    return UpdateOrderStatus(service=order_service)


def test_handle_when_order_status_is_completed_then_returned_order_status_is_completed(
    sut: UpdateOrderStatus, mocker: MockerFixture
):
    # Arrange
    order = OrderSchemaFactory(status=OrderStatus.PENDING)
    sut.service.get_by_id = mocker.Mock(return_value=order)

    # Action
    updated_order = sut.handle(order.id, OrderStatus.COMPLETED)

    # Assert
    updated_order.status == OrderStatus.COMPLETED
