from osprey.voice import Context, insert, press

from ..utils import normalize_keys

delimiters_map = normalize_keys({
    'tick': '``',
    'quote': '\'\'',
    'square|bracket': '[]',
    'angle': '<>',
    'double quote|double quotes': '""',
    'brace|curly': '{}',
    'paren': '()',
    'double under': '____',
})


def surround(m):
    delimiters = delimiters_map[m['delimiters']]
    insert(delimiters)
    for _i in range(len(delimiters) // 2):
        press('Left')


ctx = Context('delimiters')
ctx.set_commands({
    'surround <delimiters>': surround,
    'pair <delimiters>': lambda m: insert(delimiters_map[m['delimiters']]),
})
ctx.set_choices({
    'delimiters': delimiters_map.keys(),
})
