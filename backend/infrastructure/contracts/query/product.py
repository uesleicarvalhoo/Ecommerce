from typing import Optional, Protocol


class QueryProduct(Protocol):
    name: Optional[str]
    code: Optional[str]
    avaliable: Optional[bool]
