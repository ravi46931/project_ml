import logging
import os
from datetime import datetime

LOG_FILE= f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE)
os.makedirs(logs_path,exist_ok=True)

LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)

# The following type of message will print
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

# To check the code is working fine or not
if __name__=="__main__":
    logging.info("Logging has started")

# run python src/logger.py
# Then the following log printed in the log folder
# [ 2023-10-20 20:01:48,489 ] 20 root - INFO - Logging has started
#format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s"
