from osprey.voice import Context, insert

from ..utils import normalize_keys

operations_map = normalize_keys({
    'equal|equals': '=',
    'equivalent': '==',
    'not equal': '!=',
    'plus equal': '+=',
    'minus equal': '-=',
    'increment': '++',
    'decrement': '--',
    'less than': '<',
    'greater than': '>',
    'less than or equal': '<=',
    'greater than or equal': '>=',
    'and': '&&',
    'or': '||',
})


def operations(m):
    op = operations_map[m['operations']]
    insert(f' {op} ')


ctx = Context('operations')
ctx.set_commands({
    'op <operations>': operations,
})
ctx.set_choices({
    'operations': operations_map.keys(),
})
