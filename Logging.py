import logging
import time
from logging.handlers import RotatingFileHandler, TimedRotatingFileHandler
# logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# logging.debug('This is debug message')
# logging.info('This is an info message')
# logging.warning('This is a warning message')
# logging.error('This is an error message')
# logging.critical('This is critical message')



# # logger.info('Custom logger')

# # create handler
# stream_h = logging.StreamHandler()
# file_h = logging.FileHandler('file.log')

# # level and the format
# stream_h.setLevel(logging.WARNING)
# file_h.setLevel(logging.ERROR)

# formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
# stream_h.setFormatter(formatter)
# file_h.setFormatter(formatter)

# logger.addHandler(stream_h)
# logger.addHandler(file_h)

# logger.warning('This is a warning')
# logger.error('This is a error')

# import logging.config
# logging.config.dictConfig('logging.conf')

# logger = logging.getLogger('simpleExample')
# logger.debug('This is a debug message')
# import traceback

# try:
#     a = [1,2,3]
#     val = a[4]
# except IndexError as e:
#     logging.error("This error is %s", traceback.format_exc())


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# handler = RotatingFileHandler('app.log', maxBytes=2000, backupCount=5)
handler = TimedRotatingFileHandler('time_test.log',when='s', interval=5, backupCount=5)

logger.addHandler(handler)

for _ in range(6):
    logger.info('hello, world')
    time.sleep(5)