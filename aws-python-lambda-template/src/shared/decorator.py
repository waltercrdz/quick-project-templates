from datetime import datetime
from functools import wraps
import logging
from typing import Any, Callable

logger = logging.getLogger(__name__)

def loggeable(message: str) -> Callable:
    """
    Decorator to log the execution time of a function with a custom message.

    Args:
        message (str): Custom message to log with the duration.

    Returns:
        Callable: The wrapped function.
    """
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            start_time: datetime = datetime.now()
            try:
                result = func(*args, **kwargs)
            finally:
                end_time: datetime = datetime.now()
                duration = end_time - start_time
                logger.info(f"{message}: Duration {duration} seconds")
            return result
        return wrapper
    return decorator