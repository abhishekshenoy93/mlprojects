import logging
import os
import sys
from datetime import datetime
from pathlib import Path

def get_log_file_path():
    """
    This function returns the path to the log file. The log file is stored in the 'logs' directory with a name
    that includes the current date and time.
    """
    current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    log_file_name = f"logs_{current_time}.log"
    log_file_path = os.path.join("logs", log_file_name)
    
    # Create logs directory if it doesn't exist
    Path("logs").mkdir(parents=True, exist_ok=True)
    return log_file_path

# Configure logging
    
logging.basicConfig(
    filename=get_log_file_path(),
    format='[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S'
)

