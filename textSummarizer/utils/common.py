import os
import logging
from box.exceptions import BoxValueError
import yaml
from box import ConfigBox
from pathlib import Path
from typeguard import typechecked

# Set up basic logging configuration
logging.basicConfig(level=logging.INFO, format="[%(asctime)s: %(levelname)s: %(module)s: %(message)s]")
logger = logging.getLogger("textsummarizerlogger")

@typechecked
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """Reads a yaml file and returns a ConfigBox containing the data.

    Args:
        path_to_yaml (Path): Path like input.

    Raises:
        ValueError: If the yaml file is empty or an error occurs.

    Returns:
        ConfigBox: Loaded configuration in a ConfigBox.
    """
    try:
        with open(path_to_yaml, 'r') as yaml_file:
            content = yaml.safe_load(yaml_file)
            if content is None:
                raise ValueError("YAML file is empty")
            logger.info(f"YAML file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError as e:
        logger.error(f"Error loading YAML content: {e}")
        raise ValueError("YAML file is empty or invalid") from e
    except Exception as e:
        logger.error(f"Unexpected error reading YAML file: {e}")
        raise e

@typechecked
def create_directories(path_to_directories: list, verbose: bool = True):
    """Creates a list of directories.

    Args:
        path_to_directories (list): List of path of directories.
        verbose (bool, optional): Log creation. Defaults to True.
    """
    try:
        for path in path_to_directories:
            os.makedirs(path, exist_ok=True)
            if verbose:
                logger.info(f"Created directory at: {path}")
    except Exception as e:
        logger.error(f"Failed to create directories: {e}")
        raise RuntimeError(f"Could not create directories: {e}") from e

@typechecked
def get_size(path: Path) -> str:
    """Get size of a file in KB.

    Args:
        path (Path): Path of the file.

    Returns:
        str: Size in KB.
    """
    try:
        size_in_kb = round(os.path.getsize(path) / 1024)
        return f"~{size_in_kb} KB"
    except Exception as e:
        logger.error(f"Error getting size of file: {path}: {e}")
        raise ValueError(f"Cannot retrieve size for: {path}") from e
