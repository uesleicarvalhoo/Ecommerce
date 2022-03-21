import pytest
from pytest_mock import MockerFixture

from backend.domain.contracts import ClientService
from backend.domain.exceptions import DuplicatedDataError, NotFoundError
from backend.domain.rules.client import RegisterClient
from tests.factories.client import NewClientFactory


@pytest.fixture()
def sut(client_service: ClientService):
    return RegisterClient(client_service)


def test__check_if_email_is_already_used_return_false_when_service_raise_not_found_error(
    sut: RegisterClient, mocker: MockerFixture
):
    def raise_not_found_error(email: str):
        raise NotFoundError(f"Not found client with Email {email} not found")

    # Prepare
    email = "fake@emailfake.com"
    sut.service.get_by_email = mocker.Mock(side_effect=raise_not_found_error)

    # Arrange
    email_exists = sut._check_if_email_is_already_used(email)

    # Action/Assert
    assert email_exists is False


def test__check_if_email_is_already_used_return_true_when_service_does_not_raise_not_found_error(
    sut: RegisterClient, mocker: MockerFixture
):
    # Prepare
    email = "fake@emailfake.com"
    sut.service.get_by_email = mocker.Mock(return_value=None)

    # Arrange
    email_exists = sut._check_if_email_is_already_used(email)

    # Action/Assert
    assert email_exists is True


def test__check_if_phone_is_already_used_return_false_when_service_raise_not_found_error(
    sut: RegisterClient, mocker: MockerFixture
):
    def raise_not_found_error(phone: str):
        raise NotFoundError(f"Not found client with Phone '{phone}' not found")

    # Prepare
    phone = "99999999999"
    sut.service.get_by_phone = mocker.Mock(side_effect=raise_not_found_error)

    # Arrange
    phone_exists = sut._check_if_phone_is_already_used(phone)

    # Action/Assert
    assert phone_exists is False


def test__check_if_phone_is_already_used_return_true_when_service_does_not_raise_not_found_error(
    sut: RegisterClient, mocker: MockerFixture
):
    # Prepare
    phone = "99999999999"
    sut.service.get_by_phone = mocker.Mock(return_value=None)

    # Arrange
    phone_exists = sut._check_if_phone_is_already_used(phone)

    # Action/Assert
    assert phone_exists is True


def test_register_client_raise_duplicated_data_error_when_email_already_exists(
    sut: RegisterClient, mocker: MockerFixture
):
    # Prepare
    spy = sut._check_if_email_is_already_used = mocker.Mock(sut._check_if_email_is_already_used, return_value=True)
    sut._check_if_phone_is_already_used = mocker.Mock(sut._check_if_phone_is_already_used, return_value=False)

    # Arrange
    schema = NewClientFactory(email="fake@emailfake.com")

    # Action/Assert
    with pytest.raises(DuplicatedDataError):
        sut.handle(schema)

    spy.assert_called()


def test_register_client_raise_duplicated_data_error_when_phone_already_exists(
    sut: RegisterClient, mocker: MockerFixture
):
    # Prepare
    sut._check_if_email_is_already_used = mocker.Mock(sut._check_if_email_is_already_used, return_value=False)
    spy = sut._check_if_phone_is_already_used = mocker.Mock(sut._check_if_phone_is_already_used, return_value=True)

    # Arrange
    schema = NewClientFactory(phone=99999999999)

    # Action/Assert
    with pytest.raises(DuplicatedDataError):
        sut.handle(schema)

    spy.assert_called()


def test_register_client_handle_create_model_with_success(sut: RegisterClient, mocker: MockerFixture):
    # Prepare
    sut._check_if_email_is_already_used = mocker.Mock(sut._check_if_email_is_already_used, return_value=False)
    sut._check_if_phone_is_already_used = mocker.Mock(sut._check_if_phone_is_already_used, return_value=False)
    spy = mocker.spy(sut.service, "create")

    # Arrange
    schema = NewClientFactory()

    # Action
    sut.handle(schema)

    # Assert
    spy.assert_called_with(schema)
