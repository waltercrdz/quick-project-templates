from datetime import datetime
import logging
import traceback
from typing import Any, Dict

logger = logging.getLogger(__name__)

def lambda_handler(event: Dict[str, Any], _: Any) -> None:
    try:
        start_date: datetime = datetime.now()
        logger.info(f"Finished cron in {datetime.now() - start_date} seconds")
    except Exception as e:
        logger.error(
            f"There was an error while the batch processing:\n"
            f"{str(traceback.format_exc())}"
        )
        raise e
