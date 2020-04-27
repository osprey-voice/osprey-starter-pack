from sys import platform
from shutil import which
import subprocess

from osprey.voice import Context, press


def is_program_installed(name):
    """Check whether `name` is in PATH and marked as executable."""
    return which(name) is not None


def set_volume(n):
    if platform == 'win32':
        pass
    elif platform == 'darwin':
        pass
    else:
        if is_program_installed('pamixer'):
            subprocess.run(f'pamixer --set-volume {n}'.split())


ctx = Context('volume')
ctx.set_rules({
    'volume up': lambda m: press('VolumeUp'),
    'volume down': lambda m: press('VolumeDown'),
    'volume mute': lambda m: press('Mute'),
    'volume set <n>': lambda m: set_volume(m['n']),
})
