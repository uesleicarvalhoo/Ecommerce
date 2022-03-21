from typing import List
from uuid import UUID

from pydantic import BaseModel, PositiveInt

from backend.helpers.constants import SaleType


class NewOrderItemSchema(BaseModel):
    id: UUID
    amount: PositiveInt


class NewOrderSchema(BaseModel):
    description: str
    sale_type: SaleType
    items: List[NewOrderItemSchema]
