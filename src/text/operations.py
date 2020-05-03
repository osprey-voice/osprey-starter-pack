from osprey.voice import Context, insert, press

from ..utils import normalize_keys

operations_map = normalize_keys({
    'equal|equals': '=',
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
