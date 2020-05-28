from osprey.voice import Context, insert

from ..utils import normalize_keys

operators_map = normalize_keys({
    'equal|equals': '=',

    # arithmetic assignment
    'plus equal': '+=',
    'minus equal': '-=',
    'increment': '++',
    'decrement': '--',
    'multiply equal|star equal': '*=',
    'divide equal|div equal': '/=',
    'mod equal|remainder equal': '%=',

    # bitwise assignment
    'bitwise and equal': '&=',
    'bitwise or equal': '|=',
    'bitwise x or equal': '^=',
    'right shift equal': '>>=',
    'left shift equal': '<<=',

    # arithmetic expressions
    'plus': '+',
    'minus': '-',
    'multiply|star': '*',
    'divide|div': '/',
    'mod|remainder': '%',

    # bitwise expressions
    'bitwise and': '&',
    'bitwise or': '|',
    'bitwise x or': '^',
    'right shift': '>>',
    'left shift': '<<',

    # boolean expressions
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
