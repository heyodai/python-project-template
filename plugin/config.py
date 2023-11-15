import configparser
import os

CONFIG_FILE = os.path.expanduser("~/.github-labels.ini")

def get_github_api_key() -> str:
    """
    Get the GitHub API key from the config file

    Returns
    -------
    str
        The GitHub API key

    Raises
    ------
    OSError
        If the config file could not be read
    """
    config = configparser.ConfigParser()
    config.read(CONFIG_FILE)

    try:
        return config["github"]["api_key"]
    except KeyError:
        raise OSError("Could not read config file")

def set_github_api_key(key: str) -> None:
    """
    Set the GitHub API key in the config file

    Parameters
    ----------
    key : str
        The GitHub API key

    Raises
    ------
    OSError
        If the config file could not be written to
    """
    config = configparser.ConfigParser()
    config.read(CONFIG_FILE)
    config["github"] = {"api_key": key}

    try:
        with open(CONFIG_FILE, "w") as configfile:
            config.write(configfile)
    except OSError:
        raise OSError("Could not write to config file")