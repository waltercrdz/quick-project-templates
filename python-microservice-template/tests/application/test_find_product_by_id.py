import pytest
from unittest.mock import Mock
from app.application.find_product_by_id import FindProductById
from app.domain.product import Product
from app.domain.exceptions import ProductNotFoundException
from app.infrastructure.repository.product_repository import ProductRepository
from tests.utils.object_mother import PRODUCT_ID, ProductObjectMother

@pytest.fixture
def product_repository() -> Mock:
    return Mock(spec=ProductRepository)

@pytest.fixture
def find_product_by_id(product_repository: Mock) -> FindProductById:
    return FindProductById(product_repository)

def test_when_product_is_found_then_return_product(
        find_product_by_id: FindProductById,
        product_repository: Mock
) -> None:
    product: Product = ProductObjectMother.create()
    product_repository.find_by_id.return_value = product
    result = find_product_by_id.execute(product.id)
    assert result == product
    product_repository.find_by_id.assert_called_once_with(product.id)

def test_when_user_is_not_found_then_raise_user_not_found(
        find_product_by_id: FindProductById,
        product_repository: Mock
) -> None:
    product_repository.find_by_id.return_value = None
    with pytest.raises(ProductNotFoundException):
        find_product_by_id.execute(PRODUCT_ID)
    product_repository.find_by_id.assert_called_once_with(PRODUCT_ID)