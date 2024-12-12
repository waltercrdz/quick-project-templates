from decimal import Decimal
from pydantic import BaseModel

class ProductCreationRequest(BaseModel):
    name: str
    description: str
    price: Decimal
    stock: int