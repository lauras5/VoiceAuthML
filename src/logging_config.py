import logging
import sys
import traceback
from paths import DIR_PATH

logging.basicConfig(
    filename=f'{DIR_PATH}logs/error.log',
    level=logging.ERROR,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)

def log_exception(exc_type, exc_value, exc_traceback):
    logger.error("Uncaught exception", exc_info=(exc_type, exc_value, exc_traceback))

# Install the exception hook
sys.excepthook = log_exception