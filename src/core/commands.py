import subprocess
from sys import platform

from osprey.voice import Context

from ..utils import is_program_running


def clear_notifications(m):
    if platform == 'win32':
        pass
    elif platform == 'darwin':
        pass
    else:
        if is_program_running('mako'):
            subprocess.run('makoctl dismiss -a'.split())


ctx = Context('commands')
ctx.set_commands({
    'clear notifications': clear_notifications,
})
