from typing import runtime_checkable
from uuid import uuid4

import pytest

from backend.domain.contracts import AuthenticationService, TokenData
from backend.domain.rules.auth.parse_token_data import ParseTokenData


@pytest.fixture()
def sut(authentication_service: AuthenticationService):
    return ParseTokenData(authentication_service)


def test_handle_load_token_data_correctly(sut: ParseTokenData, authentication_service: AuthenticationService):
    # Arrange
    client_id = uuid4()
    scope = "myscope"
    token = authentication_service.generate_token(client_id, scope=scope)

    # Action
    token_data = sut.handle(token.access_token)

    # Assert
    assert token_data.client_id == client_id
    assert token_data.scope == scope


def test_return_implements_token_data_protocol(sut: ParseTokenData, authentication_service: AuthenticationService):
    # Arrange
    client_id = uuid4()
    token = authentication_service.generate_token(client_id)
    token_data_protocol = runtime_checkable(TokenData)

    # Action
    token_data = sut.handle(token.access_token)

    # Assert
    assert isinstance(token_data, token_data_protocol)
