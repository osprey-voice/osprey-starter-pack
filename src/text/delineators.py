from osprey.voice import Context, insert, press

from ..utils import normalize_keys

delineators_map = normalize_keys({
    'tick': '``',
    'quote': '\'\'',
    'square|bracket': '[]',
    'angle': '<>',
    'double quote|double quotes': '""',
    'brace|curly': '{}',
    'paren': '()',
})


def surround(m):
    insert(delineators_map[m['delineators']])
    press('Left')


ctx = Context('delineators')
ctx.set_commands({
    'surround <delineators>': surround,
    'pair <delineators>': lambda m: insert(delineators_map[m['delineators']]),
})
ctx.set_choices({
    'delineators': delineators_map.keys(),
})
