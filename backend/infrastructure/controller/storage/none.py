class NoneStorage:
    def upload(self, key: str, binary: bytes) -> str:
        return key  # pragma: no cover

    def delete(self, key: str) -> None:
        pass  # pragma: no cover
