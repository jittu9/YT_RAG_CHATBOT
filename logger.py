import logging
import os

LOG_DIR = "logs"
LOG_FILE = "app.log"

def setup_logger():
    os.makedirs(LOG_DIR, exist_ok=True)

    log_path = os.path.join(LOG_DIR, LOG_FILE)

    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    # جلوگیری duplicate handlers
    if not logger.handlers:

        # File handler
        file_handler = logging.FileHandler(log_path)
        file_handler.setLevel(logging.INFO)

        # Console handler
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)

        formatter = logging.Formatter(
            "%(asctime)s - %(levelname)s - %(name)s - %(message)s"
        )

        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)

        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

    return logger