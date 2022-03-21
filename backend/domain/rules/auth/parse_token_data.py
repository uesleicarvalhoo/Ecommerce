from backend.domain.contracts import AuthenticationService
from backend.domain.schemas import TokenData


class ParseTokenData:
    def __init__(self, authentication: AuthenticationService):
        self.auth = authentication

    def handle(self, raw_token: str) -> TokenData:
        return self.auth.load_token(raw_token)
