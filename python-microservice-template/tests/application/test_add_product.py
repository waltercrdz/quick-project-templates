import pytest
from unittest.mock import Mock
from tests.utils.object_mother import ProductObjectMother
from app.domain.product import Product
from app.domain.exceptions import DatabaseExecutionException
from app.application.add_product import AddProduct
from app.infrastructure.persistence.product_repository import ProductRepository

@pytest.fixture
def repository() -> Mock:
    return Mock(spec=ProductRepository)

@pytest.fixture
def service(repository: Mock) -> AddProduct:
    return AddProduct(
        repository=repository
    )

def test_when_add_product_execution_is_successful(
    service: AddProduct, repository: Mock
) -> None:
    product: Product = ProductObjectMother.create()
    repository.save.return_value = None
    
    service.execute(product)

    repository.save.assert_called_once_with(product)

def test_when_add_product_fails_then_raise_exception(
    service: AddProduct, repository: Mock
) -> None:
    product: Product = ProductObjectMother.create()
    repository.save.side_effect = DatabaseExecutionException()
    with pytest.raises(DatabaseExecutionException):
        service.execute(product)
    repository.save.assert_called_once()