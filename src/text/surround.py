from osprey.voice import Context, insert, press

from ..utils import normalize_keys

surround_map = normalize_keys({
    'tick': '``',
    'quote': '\'\'',
    'square|bracket': '[]',
    'angle': '<>',
    'double quote|double quotes': '""',
    'brace|curly': '{}',
    'paren': '()',
})


def surround(m):
    insert(surround_map[m['surround']])
    press('Left')


ctx = Context('surround')
ctx.set_commands({
    'surround <surround>': surround,
})
ctx.set_lists({
    'surround': surround_map.keys(),
})
