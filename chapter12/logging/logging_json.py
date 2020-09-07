import os
import json
import logging.config

path = 'logging.json'
if os.path.exists(path):
    with open(path, 'rt') as f:
        config = json.load(f)
        logging.config.dictConfig(config)
else:
    logging.basicConfig(level=logging.INFO)


logger = logging.getLogger('root')
logger.debug("FileHandler message")
logger.info("message for both handlers")
