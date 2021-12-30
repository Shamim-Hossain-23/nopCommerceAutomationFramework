import inspect
import logging

class LogGen:

    @staticmethod
    def loggen():
        logging.basicConfig(filename="automation.log", format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                                           datefmt='%m/%d/%Y %I:%M:%S %p')
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger

    def custom_logger(logLevel=logging.DEBUG):

        logger_name = inspect.stack()[1][3]
        # create logger
        logger = logging.getLogger(logger_name)
        logger.setLevel(logLevel)

        # create console handler and set level to debug
        ch = logging.StreamHandler()
        ch.setLevel(logLevel)

        # ALSO USE FILE HANDLER
        fh = logging.FileHandler(".\\Logs\\automation.log")

        # create formatter
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        formatter1 = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                                       datefmt='%m/%d/%Y %I:%M:%S %p')

        # add formatter to ch
        ch.setFormatter(formatter)
        fh.setFormatter(formatter1)

        # add ch to logger
        logger.addHandler(ch)
        logger.addHandler(fh)
        return logger