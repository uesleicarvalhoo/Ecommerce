from pydantic import BaseModel


class NewClientSchema(BaseModel):
    name: str
    email: str
    phone: str
    password: str
