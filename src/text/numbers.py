from osprey.voice import Context, insert

from ..utils import normalize_keys

separators_map = normalize_keys({
    'commas': ',',
    'underscores': '_',
    'dots|periods|points': '.',
})


def ordinal_suffix(n):
    suffix = ['th', 'st', 'nd', 'rd', 'th'][min(n % 10, 4)]
    if 11 <= (n % 100) <= 13:
        suffix = 'th'
    return suffix


def format_number(n, separator):
    n = str(n)
    if not separator:
        return n
    n = list(n)
    for i in range(3, len(n), 4):
        n.insert(len(n) - i, separator)
    return ''.join(n)


def number(m):
    n = m['n']
    separator = separators_map[m['separators']] if m['separators'] else None
    return format_number(n, separator)


ctx = Context('numbers')
ctx.set_commands({
    'number <n> [with <separators>]': lambda m: insert(number(m)),
    'ordinal <n> [with <separators>]': lambda m: insert(number(m) + ordinal_suffix(m['n'])),
})
ctx.set_choices({
    'separators': separators_map.keys(),
})
