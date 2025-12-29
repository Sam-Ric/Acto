"""
This module contains utility functions that can be used to
simply tasks in the other modules.
"""

import os
import tomllib

def load_config() -> dict:
    """
    Load and return the project's TOML config as a dict.
    """
    root = os.path.dirname(os.path.dirname(__file__))
    path = os.path.abspath(os.path.join(root, "config.toml"))

    with open(path, "rb") as f:
        config = tomllib.load(f)

    return config