from typing import runtime_checkable

import pytest
from pytest_mock import MockerFixture

from backend.domain.contracts import AuthenticationService, ClientService, Token
from backend.domain.exceptions import AuthorizationError
from backend.domain.rules.auth.authenticate_login import AuthenticateLogin
from tests.factories import ClientSchemaFactory


@pytest.fixture()
def sut(client_service: ClientService, authentication_service: AuthenticationService) -> AuthenticateLogin:
    return AuthenticateLogin(service=client_service, authentication=authentication_service)


def test_handle_return_a_valid_token(
    sut: AuthenticateLogin, authentication_service: AuthenticationService, mocker: MockerFixture
):
    # Arrange
    client = ClientSchemaFactory()
    password = "my_super_secret_password"
    client.password_hash = authentication_service.generate_password_hash(password)
    sut.service.get_by_email = mocker.Mock(return_value=client)

    # Action
    token = sut.handle(client.email, password)

    # Assert
    assert authentication_service.load_token(token.access_token)


def test_when_client_email_and_password_hash_is_valid_then_return_access_token_with_current_client_id(
    sut: AuthenticateLogin, authentication_service: AuthenticationService, mocker: MockerFixture
):
    # Arrange
    client = ClientSchemaFactory()
    password = "my_super_secret_password"
    client.password_hash = authentication_service.generate_password_hash(password)
    sut.service.get_by_email = mocker.Mock(return_value=client)

    # Action
    token = sut.handle(client.email, password)
    token_data = authentication_service.load_token(token.access_token)

    # Assert
    assert token_data.client_id == client.id


def test_when_password_is_invalid_then_raises_authorization_error(
    sut: AuthenticateLogin, authentication_service: AuthenticationService, mocker: MockerFixture
):
    # Arrange
    client = ClientSchemaFactory()
    invalid_password = "my_invalid_password"
    password = "my_super_secret_password"
    client.password_hash = authentication_service.generate_password_hash(password)
    sut.service.get_by_email = mocker.Mock(return_value=client)

    # Action/Assert
    with pytest.raises(AuthorizationError):
        sut.handle(client.email, invalid_password)


def test_handle_return_implements_token_protocol(
    sut: AuthenticateLogin, authentication_service: AuthenticationService, mocker: MockerFixture
):
    # Arrange
    client = ClientSchemaFactory()
    password = "my_super_secret_password"
    token_protocol = runtime_checkable(Token)
    client.password_hash = authentication_service.generate_password_hash(password)
    sut.service.get_by_email = mocker.Mock(return_value=client)

    # Action
    token = sut.handle(client.email, password)

    # Assert
    assert isinstance(token, token_protocol)
