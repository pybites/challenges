"""
log_init.py

Initializes logging for the project.
"""
import json
import logging.config
import os
from typing import Optional


def setup_logging(
    default_path: str = "logging.json",
    default_level=logging.INFO,
    env_key: str = "LOG_CFG",
):
    """Setup logging configuration"""
    path: str = default_path
    value: Optional[str] = os.getenv(env_key, None)
    if value:
        path = value
    if os.path.exists(path):
        with open(path, "rt") as f:
            config = json.load(f)
        logging.config.dictConfig(config)
    else:
        logging.basicConfig(level=default_level)

    return logging
