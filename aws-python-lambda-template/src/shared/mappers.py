
from decimal import Decimal
import json
import logging
from typing import Any
from uuid import UUID
from src.domain.product import Product

logger = logging.getLogger(__name__)

def map_to_product(record: dict[str, Any]) -> Product:
    logger.info(f"Record received: {str(record)}")
    payload = json.loads(record["body"])
    logger.debug(f"Message body: {str(payload)}")
    return Product(
        id=UUID(payload.get("id")),
        name=payload.get("name"),
        description=payload.get("description"),
        price=Decimal(payload.get("price")),
        stock=int(payload.get("stock"))
    )