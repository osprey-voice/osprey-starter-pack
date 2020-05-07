from osprey.control import disable, quit_program, reload_scripts
from osprey.open import open_config_dir, open_history_file, open_log_file
from osprey.voice import Context

ctx = Context('osprey_commands')
ctx.set_commands({
    'osprey disable': lambda m: disable(),
    'osprey quit': lambda m: quit_program(),

    'reload scripts': lambda m: reload_scripts(),

    'open (config|configuration) (dir|directory)': lambda m: open_config_dir(),
    'open history file': lambda m: open_history_file(),
    'open log file': lambda m: open_log_file(),
})
