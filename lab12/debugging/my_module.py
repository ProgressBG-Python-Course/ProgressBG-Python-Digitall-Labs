import logging

# Initialize logger
logger = logging.getLogger('my_module')
logger.setLevel(logging.DEBUG)

# Configure console handler
console_handler = logging.StreamHandler()

# Configure formatter
formatter = logging.Formatter('%(name)s:%(levelname)s:%(message)s')
console_handler.setFormatter(formatter)

# Add console handler to logger
logger.addHandler(console_handler)

def add(x,y):
    logger.info('Add starts')
    logger.debug(type(x))
    logger.debug(type(y))

    print(x+y)