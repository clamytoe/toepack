"""
log_init.py

Initializes logging for the project.
"""
import os
import json
import logging.config
from pathlib import Path


MODULE_PATH = Path(__file__).resolve().parent
LOG_CONFIG = MODULE_PATH.joinpath("logging.json")


def setup_logging(
    default_path=LOG_CONFIG, default_level=logging.INFO, env_key="LOG_CFG"
):
    """Setup logging configuration"""
    path = default_path
    value = os.getenv(env_key, None)
    if value:
        path = Path(value)
    if path.is_file():
        config = json.loads(path.read_text())
        logging.config.dictConfig(config)
    else:
        logging.basicConfig(level=default_level)

    return logging
