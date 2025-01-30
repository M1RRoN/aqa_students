import logging
import os


class Logger:
    def __init__(self, name=__name__):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.INFO)

        log_directory = os.path.join(os.getcwd(), 'logs')
        if not os.path.exists(log_directory):
            os.makedirs(log_directory)

        log_file = os.path.join(log_directory, 'tests.log')

        file_handler = logging.FileHandler(log_file, mode='a')
        file_handler.setLevel(logging.INFO)
        file_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
        self.logger.addHandler(file_handler)

        stream_handler = logging.StreamHandler()
        stream_handler.setLevel(logging.INFO)
        stream_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
        self.logger.addHandler(stream_handler)

    def info(self, message):
        self.logger.info(message)

    def debug(self, message):
        self.logger.debug(message)

    def warning(self, message):
        self.logger.warning(message)

    def error(self, message):
        self.logger.error(message)

    def critical(self, message):
        self.logger.critical(message)
