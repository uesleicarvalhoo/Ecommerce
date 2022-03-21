from typing import Protocol
from uuid import UUID

from backend.domain.contracts import Token, TokenData


class AuthenticationService(Protocol):
    def generate_password_hash(self, password: str) -> str:
        ...  # pragma: no cover

    def check_password_hash(self, password: str, password_hash: str) -> bool:
        ...  # pragma: no cover

    def generate_token(self, client_id: UUID, expires_in: int = 60, scope: str = None) -> Token:
        ...  # pragma: no cover

    def load_token(self, raw_token: str) -> TokenData:
        ...  # pragma: no cover
