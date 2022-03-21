from typing import Protocol

from backend.domain.contracts import Client, Order


class EmailService(Protocol):
    def send_new_order_email(self, client: Client, order: Order) -> None:
        ...  # pragma: no cover

    def send_recovery_password_email(self, client: Client) -> None:
        ...  # pragma: no cover
