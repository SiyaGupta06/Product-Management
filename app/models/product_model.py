from pydantic import BaseModel


class ProductCreate(BaseModel):

    id: int
    name: str
    price: float
    quantity: int