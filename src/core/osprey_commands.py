from osprey.voice import Context
from osprey.control import disable, quit_program
from osprey.open import open_config_dir, open_log_file, open_history_file

ctx = Context('osprey_commands')
ctx.set_commands({
    'osprey disable': lambda m: disable(),
    'osprey quit': lambda m: quit_program(),

    'open (config|configuration) (dir|directory)': lambda m: open_config_dir(),
    'open log file': lambda m: open_log_file(),
    'open history file': lambda m: open_history_file(),
})
