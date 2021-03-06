"""
This module is used for typing out words that are already in the model vocabulary but are difficult
for the engine to identify because they get confused with other words.
"""

from osprey.voice import Context, insert

fix_list = [
    'add',
    'and',
    'bin',
    'crate',
    'desk',
    'git',
    'man',
]

ctx = Context('fix')
ctx.set_commands({
    'fix <fix>': lambda m: insert(m['fix']),
    'fix upper <fix>': lambda m: insert(m['fix'].capitalize()),
})
ctx.set_choices({
    'fix': fix_list,
})
