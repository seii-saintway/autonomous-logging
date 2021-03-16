
import logging

print(logging.root.manager.loggerDict)

logger = logging.getLogger('test_logging')
logger.setLevel(logging.DEBUG)

logger.addHandler(logging.FileHandler('my_test_logging.log'))

if __name__ == '__main__':
    import test_logging
    print(test_logging.__name__)
