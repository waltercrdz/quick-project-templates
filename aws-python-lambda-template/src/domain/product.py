from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal
from typing import Any
from uuid import UUID

@dataclass
class Product:
    id: UUID
    name: str
    description: str
    price: Decimal
    stock: int
    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()

    def to_dict(self) -> dict[str, Any]:
        return {
            "id": str(self.id),
            "name": self.name,
            "description": self.description,
            "price": str(self.price),
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat()
        }