import logging
import os
from datetime import datetime

LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
log_path=os.path.join(os.getcwd(),"logs",LOG_FILE)
os.makedirs(log_path,exist_ok=True)

LOG_FILE_PATH=os.path.join(log_path,LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

if __name__=="__main__":
    logging.info("Logging has started successfully!")
    
    
# This ensures that every time you run the project, you get a brand-new file. You never accidentally overwrite your old history!
# LOG_FILE = unique log file name based on timestamp
#It creates a full path only path .no folder created ..just a name logs created by joining 3 parts: log_path = full path of log file  C:\Users\...\ML_project\logs\03_24_2026_21_30_45.log
# You are trying to create a folder with file name (.log)
# LOG_FILE_PATH = os.path.join(log_path, LOG_FILE)  .../logs/03_24_2026.log/03_24_2026.log
