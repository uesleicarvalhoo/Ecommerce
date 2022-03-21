from backend.domain.contracts import AuthenticationService, ClientService, Token
from backend.domain.exceptions import AuthorizationError


class AuthenticateLogin:
    def __init__(self, service: ClientService, authentication: AuthenticationService) -> None:
        self.service = service
        self.auth = authentication

    def handle(self, email: str, password: str) -> Token:
        client = self.service.get_by_email(email)

        if not self.auth.check_password_hash(password, client.password_hash):
            raise AuthorizationError("Credenciais invalidas!")

        return self.auth.generate_token(client.id)
