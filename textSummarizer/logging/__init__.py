import os
import sys
import logging

# Define the logging format string
logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"
# Define the directory for logs
log_dir = "logs"
# Create the full file path for the logs
log_filepath = os.path.join(log_dir, "running_logs.log")
# Ensure the directory exists
os.makedirs(log_dir, exist_ok=True)

# Configure logging with multiple handlers
logging.basicConfig(
    level=logging.INFO,  # Set the logging level to INFO
    format=logging_str,  # Use the defined format string
    handlers=[
        logging.FileHandler(log_filepath),  # Log to a file
        logging.StreamHandler(sys.stdout)   # Also log to standard output
    ]
)

# Get a logger instance for the application
logger = logging.getLogger("textsummarizerlogger")
