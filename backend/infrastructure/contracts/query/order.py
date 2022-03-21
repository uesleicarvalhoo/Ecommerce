from typing import Optional, Protocol
from uuid import UUID


class QueryOrder(Protocol):
    id: Optional[UUID]
