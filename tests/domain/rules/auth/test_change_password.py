import pytest
from pytest_mock import MockerFixture

from backend.domain.contracts import AuthenticationService, ClientService
from backend.domain.rules.auth.change_password import ChangePassword
from tests.factories import ClientSchemaFactory


@pytest.fixture()
def sut(client_service: ClientService, authentication_service: AuthenticationService):
    return ChangePassword(client_service, authentication_service)


def test_handle_after_change_password_authentication_check_password_hash_return_true_for_new_password(
    sut: ChangePassword, authentication_service: AuthenticationService, mocker: MockerFixture
):
    # Arrange
    new_passwod = "my_new_password!"
    client = ClientSchemaFactory()
    sut.service.get_by_id = mocker.Mock(return_value=client)

    # Action
    sut.handle(client.id, new_password=new_passwod)

    # Assert
    assert authentication_service.check_password_hash(new_passwod, client.password_hash)


def test_handle_save_client_after_password_change(
    sut: ChangePassword, authentication_service: AuthenticationService, mocker: MockerFixture
):
    # Arrange
    new_passwod = "my_new_password!"
    client = ClientSchemaFactory()
    sut.service.get_by_id = mocker.Mock(return_value=client)
    spy = mocker.spy(sut.service, "save")

    # Action
    sut.handle(client.id, new_password=new_passwod)

    # Assert
    spy.assert_called_with(client)
