from typing import Optional, Protocol
from uuid import UUID


class QueryClient(Protocol):
    id: Optional[UUID]
    email: Optional[str]
    phone: Optional[str]
