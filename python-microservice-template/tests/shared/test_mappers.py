from app.shared.mappers import map_to_product
from app.domain.product import Product
from tests.utils.object_mother import ProductCreationRequestObjectMother
import tests.utils.object_mother as object_mother

def test_map_to_product() -> None:
    product_creation_request = ProductCreationRequestObjectMother.create()

    product: Product = map_to_product(product_creation_request, object_mother.PRODUCT_ID)

    assert product.id == object_mother.PRODUCT_ID
    assert product.name == object_mother.PRODUCT_NAME
    assert product.description == object_mother.PRODUCT_DESCRIPTION
    assert product.price == object_mother.PRODUCT_PRICE
    assert product.stock == object_mother.PRODUCT_STOCK