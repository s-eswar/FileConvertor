import os
from src.utils.logging_utils import configure_logging

# Configure logging
configure_logging()
import logging

def create_directory(directory_path):
    """Create a directory if it doesn't exist."""
    try:
        os.makedirs(directory_path, exist_ok=True)
        logging.info(f"Directory created or already exists: {directory_path}")
    except Exception as e:
        logging.error(f"Failed to create directory '{directory_path}': {e}")
        raise