from typing import Dict, Union


class BaseDomainException(Exception):
    def __init__(self, message: Union[str, Dict[str, str]]) -> None:
        self.detail = message
        super().__init__(message)


class NotFoundError(BaseDomainException):
    pass  # pragma: no cover


class DuplicatedDataError(BaseDomainException):
    pass  # pragma: no cover
