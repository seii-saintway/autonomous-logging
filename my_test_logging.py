
import logging

print(f'logging.root.manager.loggerDict = {logging.root.manager.loggerDict}')

logger = logging.getLogger('test_logging')
print(f'logging.root.manager.loggerDict = {logging.root.manager.loggerDict}')

logger.setLevel(logging.DEBUG)

logger.addHandler(logging.FileHandler('my_test_logging.log'))

if __name__ == '__main__':
    import test_logging
    print(f'test_logging.__name__ = {test_logging.__name__}')
    print(f'logging.root.manager.loggerDict = {logging.root.manager.loggerDict}')
