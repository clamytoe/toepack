"""
log_init.py

Initializes logging for the project.
"""
import os
import json
import logging.config


module_path = __file__
pwd = "/".join(module_path.split("/")[:-1])
filename = "logging.json"
log_config = os.path.join(pwd, filename)


def setup_logging(
    default_path=log_config, default_level=logging.INFO, env_key="LOG_CFG"
):
    """Setup logging configuration"""
    path = default_path
    value = os.getenv(env_key, None)
    if value:
        path = value
    if os.path.exists(path):
        with open(path, "rt") as f:
            config = json.load(f)
        logging.config.dictConfig(config)
    else:
        logging.basicConfig(level=default_level)

    return logging
