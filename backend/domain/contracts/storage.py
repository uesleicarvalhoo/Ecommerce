from typing import Protocol


class Storage(Protocol):
    def upload(self, key: str, binary: bytes) -> str:
        ...  # pragma: no cover

    def delete(self, key: str) -> None:
        ...  # pragma: no cover
