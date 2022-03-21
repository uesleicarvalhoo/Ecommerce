from typing import Optional, Protocol
from uuid import UUID


class Token(Protocol):
    access_token: str
    grant_type: str
    exp: int
    scope: Optional[str]


class TokenData(Protocol):
    client_id: UUID
    scope: Optional[str]
