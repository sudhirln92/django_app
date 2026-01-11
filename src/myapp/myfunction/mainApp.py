import logging

logger = logging.getLogger("django_logs")


class MainApp:
    """
    Data pipeline

    """

    def __init__(self, key: dict, key2: dict, **kwargs) -> None:
        self.key = key
        self.key2 = key2

    def pipeline(self, data):
        logger.info("pipeline")
        pass
