from typing import Optional
from uuid import UUID

from pydantic import BaseModel


class QueryProductSchema(BaseModel):
    id: Optional[UUID]
    name: Optional[str]
    code: Optional[str]
    avaliable: Optional[bool]
