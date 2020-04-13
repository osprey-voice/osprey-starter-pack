from osprey.voice import Context
from osprey.control import disable, quit_program

ctx = Context('control')
ctx.set_rules({
    'disable': lambda m: disable(),
    'quit': lambda m: quit_program(),
})
