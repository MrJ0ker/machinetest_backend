import logging
from django.conf import settings

class ErrorLogger(object):
    def __init__(self):
            # Create the Logger
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.ERROR)

        # Create the Handler for logging data to a file
        logger_handler = logging.FileHandler(settings.BASE_DIR+'/log/error_log.log')
        logger_handler.setLevel(logging.ERROR)

        # Create a Formatter for formatting the log messages
        logger_formatter = logging.Formatter('%(asctime)s - %(pathname)s - %(lineno)d - %(module)s - %(funcName)s - %(levelname)s - %(message)s - %(user)s - %(details)s')

        # Add the Formatter to the Handler
        logger_handler.setFormatter(logger_formatter)

        # Add the Handler to the Logger
        self.logger.addHandler(logger_handler)
