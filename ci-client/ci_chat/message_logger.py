import logging


class MessageLogger:
    logging.basicConfig(level=logging.INFO)

    @staticmethod
    def log(message: str) -> None:
        logging.info(f"Message: {message}")
