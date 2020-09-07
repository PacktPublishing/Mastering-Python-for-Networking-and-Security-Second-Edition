import logging

try:
    open('/path/to/does/not/exist', 'rb')
except Exception as exception:
    logging.error('Failed to open file', exc_info=True)
    logging.exception('Failed to open file')
