import os
import logging
import json

def setup_logging(debug):
    log_level = logging.DEBUG if debug else logging.INFO
    logging.basicConfig(level=log_level, format='%(asctime)s - %(levelname)s - %(message)s')
    log("INFO", "Logging setup complete")

def log(level, message):
    if level == "DEBUG":
        logging.debug(message)
    elif level == "INFO":
        logging.info(message)
    elif level == "WARNING":
        logging.warning(message)
    elif level == "ERROR":
        logging.error(message)
    elif level == "CRITICAL":
        logging.critical(message)

def load_config():
    with open('config/murc.json', 'r') as config_file:
        config = json.load(config_file)
    return config

def ensure_dir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
