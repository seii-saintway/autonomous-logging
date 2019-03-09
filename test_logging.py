
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.NOTSET)

logger.addHandler(logging.FileHandler('test_logging.log'))

logger.warning('output something')
