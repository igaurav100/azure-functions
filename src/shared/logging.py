import logging
import json

def get_logger(name: str):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    def log(message, **kwargs):
        payload = {"message": message, **kwargs}
        logger.info(json.dumps(payload))

    return log