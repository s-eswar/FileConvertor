import pandas as pd
from src.utils.file_ops import create_directory
from src.utils.logging_utils import configure_logging
import os

# Configure logging
configure_logging()
import logging

def read_excel_file(file_path, sheet_name):
    """Read an Excel file and return a DataFrame."""
    try:
        return pd.read_excel(file_path, engine='openpyxl', sheet_name=sheet_name)
    except FileNotFoundError:
        logging.error(f"Excel file not found: {file_path}")
        raise
    except Exception as e:
        logging.error(f"Error reading Excel file '{file_path}': {e}")
        raise

def save_csv(filtered_df, output_folder, file_name):
    """Save a DataFrame as a CSV file."""
    try:
        # Ensure the output folder exists
        if not os.path.exists(output_folder):
            create_directory(output_folder)

        # Save the DataFrame as a CSV file
        file_path = os.path.join(output_folder, file_name)
        filtered_df.to_csv(file_path, index=False)
        logging.info(f"CSV saved: {file_path}")
    except Exception as e:
        logging.error(f"Error saving CSV '{file_name}': {e}")
        raise