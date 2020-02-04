from osprey.voice import Context, preferred_phrases
from osprey.control import disable, quit_program

ctx = Context("control")
ctx.set_rules({
    "disable": lambda: disable(),
    "quit": lambda: quit_program(),
})

preferred_phrases.update({"disable", "quit"})
