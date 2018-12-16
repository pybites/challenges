"""
log_init.py

Initializes logging for the project.
"""
import json
import logging.config
import os
from typing import Any, Dict, Optional

module_path: str = __file__
pwd: str = "/".join(module_path.split("/")[:-1])
filename: str = "logging.json"
log_config: str = os.path.join(pwd, filename)


def setup_logging(
    default_path: str = log_config,
    default_level: int = logging.INFO,
    env_key: str = "LOG_CFG",
) -> Any:
    """Setup logging configuration"""
    path: str = default_path
    value: Optional[str] = os.getenv(env_key, None)
    if value:
        path = value
    if os.path.exists(path):
        with open(path, "rt") as f:
            config: Dict[str, str] = json.load(f)
        logging.config.dictConfig(config)
    else:
        logging.basicConfig(level=default_level)

    return logging
