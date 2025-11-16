import logging


def get_logger(name: str, level=logging.INFO):
    """
    Simple console-only logger for consistent logging across the project.
    """
    logger = logging.getLogger(name)

    # Avoid duplicated handlers if logger already created
    if logger.handlers:
        return logger

    logger.setLevel(level)

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)-8s | %(name)s | %(message)s", "%Y-%m-%d %H:%M:%S"
    )

    console = logging.StreamHandler()
    console.setLevel(level)
    console.setFormatter(formatter)

    logger.addHandler(console)
    logger.propagate = False

    return logger
