import os
from box.exceptions import BoxValueError
import yaml
from textSummarizer.logging import logger
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any

@ensure_annotations
def read_yaml( path_to_yaml: Path) -> ConfigBox:
    """
    Read a yaml file and return a ConfigBox object.
    Raises:
          ValueError: if yaml is empty
          e: empty file
    """
    try:
        with open(path_to_yaml, "r") as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("Could not load yaml file")
    except Exception as e:
        raise e

@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """
    Create list of directories
    """
    for path in path_to_directories:
        os.makedirs(path)
        if verbose:
            logger.info(f"creating directory: {path}")

@ensure_annotations
def get_size(path: Path) -> str:
    """
    Get the size of a file in KB
    """
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~{size_in_kb} KB"
