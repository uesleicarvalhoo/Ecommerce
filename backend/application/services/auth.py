from datetime import timedelta
from time import time
from uuid import UUID

from jose import jwt
from jose.exceptions import ExpiredSignatureError
from passlib.context import CryptContext
from pydantic import ValidationError

from backend.application.exceptions import AuthorizationError
from backend.application.schemas import Token, TokenData
from backend.helpers.date import get_now_datetime


class AuthenticationService:
    ALGORITHM = "HS256"

    def __init__(self, password_context: CryptContext, secret_key: str) -> None:
        self.context = password_context
        self.SECRET_KEY = secret_key

    def generate_password_hash(self, password: str) -> str:
        return self.context.hash(password)

    def check_password_hash(self, password: str, password_hash: str) -> bool:
        return self.context.verify(password, password_hash)

    def generate_token(self, client_id: UUID, expires_in: int = 60, scope: str = None) -> Token:
        now = get_now_datetime()
        expire = now + timedelta(minutes=expires_in)

        to_encode = {"exp": expire, "sub": str(client_id), "created_at": time(), "scope": scope}

        access_token = jwt.encode(to_encode, self.SECRET_KEY, algorithm=self.ALGORITHM)

        token = Token(access_token=access_token, grant_type="bearer", exp=expire.timestamp(), scope=scope)

        return token

    def load_token(self, raw_token: str) -> TokenData:
        if not raw_token:
            raise AuthorizationError("Token invalido")

        try:
            return TokenData(**jwt.decode(raw_token, self.SECRET_KEY, algorithms=[self.ALGORITHM]))

        except ExpiredSignatureError:
            raise AuthorizationError("Sessão expirada")

        except (jwt.JWTError, ValidationError):
            raise AuthorizationError("Não foi possível validar as suas credenciais")
