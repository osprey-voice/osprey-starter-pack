from osprey.voice import Context
from osprey.control import disable, quit_program

ctx = Context('osprey_control')
ctx.set_rules({
    'disable': lambda m: disable(),
    'quit': lambda m: quit_program(),
})
