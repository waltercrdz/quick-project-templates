import logging
import traceback
from typing import Any, Dict

from src.configuration.config import create_add_product
from src.domain.product import Product
from src.shared.mappers import map_to_product
from src.shared.decorator import loggeable

logger = logging.getLogger(__name__)

@loggeable("Product processing completed")
def lambda_handler(event: Dict[str, Any], _: Any) -> Dict[str, Any]:
    try:
        for record in event["Records"]:
            product: Product = map_to_product(record)
            logger.info(f"Processing a new Product: {str(product)}")
            with create_add_product() as add_product:
                add_product.execute(product)
        return {
            "statusCode": 200, 
            "body": "Products processed successfully"
        }
    except Exception as e:
        logger.error(
            f"There was an error while the batch processing:\n"
            f"{str(traceback.format_exc())}"
        )
        return {
            "statusCode": 500, 
            "body": f"There was an error while processing the products: {str(e)}"
        }
