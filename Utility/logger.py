import logging


class LogGen:
    @staticmethod
    def loggen():
        logger = logging.getLogger("Test Cases for Supervisor Role")
        fileHandler = logging.FileHandler("log_file.log", mode="w")
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)
        logger.setLevel(logging.INFO)
        return logger
