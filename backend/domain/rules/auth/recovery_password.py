from backend.domain.contracts import AuthenticationService, ClientService, EmailService


class RecoveryPassword:
    def __init__(
        self, client_service: ClientService, email_service: EmailService, authentication_service: AuthenticationService
    ) -> None:
        self.client_service = client_service
        self.email_service = email_service
        self.authentication_service = authentication_service

    def handle(self, email: str) -> None:
        client = self.client_service.get_by_email(email)
        recovery_token = self.authentication_service.generate_token(client_id=client.id, expires_in=60 * 24)
        self.email_service.send_recovery_password_email(client, recovery_token)
