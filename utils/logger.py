import logging
import os
from datetime import datetime

LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

logfile_name = f"logs_{datetime.now().strftime('%Y-%m-%d')}.logs"
logfile_path = os.path.join(LOG_DIR, logfile_name)

logging.basicConfig(
    filename=logfile_path,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

def get_logger(name:str):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    return logger

# if __name__ == "__main__":
#     get_logger("test")