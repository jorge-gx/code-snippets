# used this to set up error loggin on a side project
# used a config file to store file paths
# need to revisit to clean it up

import logging.handlers
from configparser import ConfigParser
from error_logging.error_logging import error_logging


# get config values - for file path
config = ConfigParser()
config.read('../scripts/config.ini')
apple_dep_logs_dir = str(config.get('file_paths', 'apple_dep_logs_dir'))


# BEGIN -- Set Up Logging \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Define Formatter
formatter = logging.Formatter('%(asctime)s - %(levelname)-10s: %(name)s : %(message)-50s [%(module)s.%(funcName)s()]', datefmt='%m/%d/%Y %I:%M:%S %p')
stream_formatter = logging.Formatter('>%(levelname)-10s: %(module)-30s: %(message)s')

# Setup for file_handler
file_handler = logging.handlers.RotatingFileHandler(apple_dep_logs_dir + 'get_device_data.log', maxBytes=10000, backupCount=6)
file_handler.setFormatter(formatter)
file_handler.setLevel(logging.INFO)

# Setup for stream_handler
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(stream_formatter)
stream_handler.setLevel(logging.DEBUG)

# Add handlers to logger
logger.addHandler(file_handler)
logger.addHandler(stream_handler)
# END -- Set Up Logging \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
