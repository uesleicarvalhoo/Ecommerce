import pytest
from pytest_mock import MockerFixture

from backend.application.schemas import UpdateClientSchema
from backend.domain.contracts import ClientService
from backend.domain.rules.client.update import UpdateClient
from tests.factories.client import ClientSchemaFactory


@pytest.fixture()
def sut(client_service: ClientService) -> UpdateClient:
    return UpdateClient(client_service)


def test_when_update_data_name_is_not_none_then_client_name_is_updated(sut: UpdateClient, mocker: MockerFixture):
    # Arrange
    client = ClientSchemaFactory()
    new_name = "New client name"
    update_data = UpdateClientSchema(name=new_name)
    sut.service.get_by_id = mocker.Mock(return_value=client)

    # Action
    sut.handle(client.id, update_data)

    # Assert
    assert client.name == new_name


def test_when_update_data_name_is_none_then_client_name_is_not_updated(sut: UpdateClient, mocker: MockerFixture):
    # Arrange
    client = ClientSchemaFactory()
    initial_name = client.name
    update_data = UpdateClientSchema(name=None)
    sut.service.get_by_id = mocker.Mock(return_value=client)

    # Action
    sut.handle(client.id, update_data)

    # Assert
    assert client.name == initial_name


def test_when_update_data_email_is_not_none_then_client_email_is_updated(sut: UpdateClient, mocker: MockerFixture):
    # Arrange
    client = ClientSchemaFactory()
    new_email = "email@newemail.com.br"
    update_data = UpdateClientSchema(email=new_email)
    sut.service.get_by_id = mocker.Mock(return_value=client)

    # Action
    sut.handle(client.id, update_data)

    # Assert
    assert client.email == new_email


def test_when_update_data_email_is_none_then_client_email_is_not_updated(sut: UpdateClient, mocker: MockerFixture):
    # Arrange
    client = ClientSchemaFactory()
    initial_email = client.email
    update_data = UpdateClientSchema(email=None)
    sut.service.get_by_id = mocker.Mock(return_value=client)

    # Action
    sut.handle(client.id, update_data)

    # Assert
    assert client.email == initial_email


def test_when_update_data_phone_is_not_none_then_client_phone_is_updated(sut: UpdateClient, mocker: MockerFixture):
    # Arrange
    client = ClientSchemaFactory()
    new_phone = "5500000000000"
    update_data = UpdateClientSchema(phone=new_phone)
    sut.service.get_by_id = mocker.Mock(return_value=client)

    # Action
    sut.handle(client.id, update_data)

    # Assert
    assert client.phone == new_phone


def test_when_update_data_phone_is_none_then_client_phone_is_not_updated(sut: UpdateClient, mocker: MockerFixture):
    # Arrange
    client = ClientSchemaFactory()
    initial_phone = client.phone
    update_data = UpdateClientSchema(phone=None)
    sut.service.get_by_id = mocker.Mock(return_value=client)

    # Action
    sut.handle(client.id, update_data)

    # Assert
    assert client.phone == initial_phone
