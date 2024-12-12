from uuid import UUID, uuid4
from fastapi import APIRouter, Depends
from app.configuration.config import get_add_product, get_find_product_by_id
from app.domain.product import Product
from app.infrastructure.routers.dto import ProductCreationRequest
from app.application.add_product import AddProduct
from app.application.find_product_by_id import FindProductById
from app.shared.mappers import map_to_product

router = APIRouter(
    prefix="/products",
    tags=["products"]
)


@router.post("/")
async def add_product(
    product_creation_request: ProductCreationRequest,
    add_product: AddProduct = Depends(get_add_product),
) -> dict[str, str]:
    product_id: UUID = uuid4()
    product: Product = map_to_product(product_creation_request, product_id)
    add_product.execute(product)
    return product.to_dict()

@router.get("/{product_id}")
async def get_product_by_id(
    product_id: str, 
    find_product_by_id: FindProductById = Depends(get_find_product_by_id)
) -> dict[str, str]:
    return find_product_by_id.execute(UUID(product_id)).to_dict()
