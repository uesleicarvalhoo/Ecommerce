from typing import Protocol


class Streamer(Protocol):
    def send_email(self, title: str, to: str, content: str, attachment=None) -> None:
        ...  # pragma: no cover
