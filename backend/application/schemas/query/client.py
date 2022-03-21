from typing import Optional
from uuid import UUID

from pydantic import BaseModel


class QueryClientSchema(BaseModel):
    id: Optional[UUID]
    email: Optional[str]
    phone: Optional[str]
