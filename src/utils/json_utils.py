import json
import logging

def load_config(config_path="config.json"):
    """Load configuration from a JSON file."""
    try:
        with open(config_path, "r") as config_file:
            return json.load(config_file)
    except FileNotFoundError:
        logging.error(f"Config file not found: {config_path}")
        raise
    except json.JSONDecodeError as e:
        logging.error(f"Error parsing config file: {e}")
        raise