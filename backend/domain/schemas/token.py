from typing import Optional
from uuid import UUID

from pydantic import BaseModel, Field


class Token(BaseModel):
    access_token: str
    grant_type: str
    exp: int
    scope: Optional[str]


class TokenData(BaseModel):
    client_id: UUID = Field(alias="sub")
    scope: Optional[str]
