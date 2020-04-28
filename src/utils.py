import subprocess
from shutil import which


def normalize_keys(dict):
    normalized_dict = {}
    for k, v in dict.items():
        for cmd in k.split('|'):
            normalized_dict[cmd] = v
    return normalized_dict


def is_program_running(name):
    return subprocess.run(['pgrep', name], capture_output=True).returncode == 0


def is_program_installed(name):
    """Check whether `name` is in PATH and marked as executable."""
    return which(name) is not None
