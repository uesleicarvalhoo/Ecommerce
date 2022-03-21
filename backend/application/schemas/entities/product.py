from uuid import UUID, uuid4

from pydantic import BaseModel, Field


class ProductSchema(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    code: str
    name: str
    value: float
    amount: int
    file_key: str
