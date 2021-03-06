import subprocess
from sys import platform

from osprey.voice import Context, press

from ..utils import is_program_installed


def set_volume(n):
    if platform == 'win32':
        pass
    elif platform == 'darwin':
        pass
    else:
        if is_program_installed('pamixer'):
            subprocess.run(f'pamixer --set-volume {n}'.split())


ctx = Context('volume')
ctx.set_commands({
    'volume up': lambda m: press('VolumeUp'),
    'volume down': lambda m: press('VolumeDown'),
    'volume mute': lambda m: press('VolumeMute'),
    'volume set <n>': lambda m: set_volume(m['n']),
})
