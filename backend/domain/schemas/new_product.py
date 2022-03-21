from pydantic import BaseModel


class NewProductSchema(BaseModel):
    code: str
    name: str
    value: float
    amount: int
