from osprey.voice import Context, insert

from ..utils import normalize_keys

operators_map = normalize_keys({
    'equal|equals': '=',
    'plus equal': '+=',
    'minus equal': '-=',
    'increment': '++',
    'decrement': '--',

    'equivalent': '==',
    'not equal': '!=',
    'less than': '<',
    'greater than': '>',
    'less than or equal': '<=',
    'greater than or equal': '>=',
    'and': '&&',
    'or': '||',
})


def operators(m):
    op = operators_map[m['operators']]
    insert(f' {op} ')


ctx = Context('operators')
ctx.set_commands({
    'op <operators>': operators,
})
ctx.set_choices({
    'operators': operators_map.keys(),
})
