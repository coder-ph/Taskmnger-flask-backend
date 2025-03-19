import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def log_error(error):
    logger.error(f"Error: {error}")