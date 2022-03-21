import time
from typing import runtime_checkable
from uuid import uuid4

import pytest

from backend.domain.contracts import AuthenticationService, Token
from backend.domain.exceptions import AuthorizationError
from backend.domain.rules.auth.refresh_token import RefreshToken


@pytest.fixture()
def sut(authentication_service: AuthenticationService):
    return RefreshToken(authentication_service)


def test_when_token_is_invalid_raises_authorization_error(sut: RefreshToken):
    # Arrange
    fake_invalid_token = "fake token"

    # Action/Assert
    with pytest.raises(AuthorizationError):
        sut.handle(fake_invalid_token)


def test_return_implement_token_protocol(sut: RefreshToken, authentication_service: AuthenticationService):
    # Arrange
    token_protocol = runtime_checkable(Token)
    token = authentication_service.generate_token(client_id=uuid4())

    # Action
    new_token = sut.handle(token.access_token)

    # Assert
    assert isinstance(new_token, token_protocol)


def test_return_token_expiration_is_greather_then_old_token(
    sut: RefreshToken, authentication_service: AuthenticationService
):
    # Arrange
    token = authentication_service.generate_token(client_id=uuid4())

    # Action
    time.sleep(1)
    new_token = sut.handle(token.access_token)

    # Assert
    assert new_token.exp > token.exp


def test_return_token_contains_same_client_id(sut: RefreshToken, authentication_service: AuthenticationService):
    # Arrange
    client_id = uuid4()
    token = authentication_service.generate_token(client_id=client_id)

    # Action
    new_token = sut.handle(token.access_token)
    new_token_data = authentication_service.load_token(new_token.access_token)

    # Assert
    assert new_token_data.client_id == client_id


def test_return_token_contains_same_scope(sut: RefreshToken, authentication_service: AuthenticationService):
    # Arrange
    client_id = uuid4()
    scope = "myscope"
    token = authentication_service.generate_token(client_id=client_id, scope=scope)

    # Action
    new_token = sut.handle(token.access_token)
    new_token_data = authentication_service.load_token(new_token.access_token)

    # Assert
    assert new_token_data.scope == scope
