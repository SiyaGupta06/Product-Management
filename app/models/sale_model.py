from pydantic import BaseModel


class SaleCreate(BaseModel):

    quantity: int