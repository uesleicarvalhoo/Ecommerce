from pydantic import BaseModel


class UpdateClientSchema(BaseModel):
    name: str = None
    email: str = None
    phone: str = None
