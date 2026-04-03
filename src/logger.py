import logging
import os
from datetime import datetime

# Step 1: create logs folder ONLY
LOG_DIR = os.path.join(os.getcwd(), "logs")
os.makedirs(LOG_DIR, exist_ok=True)

# Step 2: correct file name (NO SPACE)
LOG_FILE = f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"

# Step 3: full file path
LOG_FILE_PATH = os.path.join(LOG_DIR, LOG_FILE)

# Step 4: logging config
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

if __name__ == "__main__":
    logging.info("Logging has started")