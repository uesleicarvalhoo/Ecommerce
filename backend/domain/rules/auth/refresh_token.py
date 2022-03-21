from backend.domain.contracts import AuthenticationService, Token


class RefreshToken:
    def __init__(self, authentication: AuthenticationService) -> None:
        self.auth = authentication

    def handle(self, raw_token: str) -> Token:
        data = self.auth.load_token(raw_token)

        return self.auth.generate_token(data.client_id, scope=data.scope)
