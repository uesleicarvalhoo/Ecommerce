from typing import Optional
from uuid import UUID

from pydantic import BaseModel


class QueryOrderSchema(BaseModel):
    id: Optional[UUID]
