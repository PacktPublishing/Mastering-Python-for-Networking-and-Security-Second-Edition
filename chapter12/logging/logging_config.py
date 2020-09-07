import logging.config
logging.config.fileConfig('logging.config')
logger = logging.getLogger('root')
logger.debug("FileHandler message")
logger.info("message for both handlers")
