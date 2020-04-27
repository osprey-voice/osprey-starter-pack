from osprey.voice import Context, insert


def ordinal(n):
    """
    Convert an integer into its ordinal representation:
        ordinal(0)   => '0th'
        ordinal(3)   => '3rd'
        ordinal(122) => '122nd'
        ordinal(213) => '213th'
    """
    suffix = ['th', 'st', 'nd', 'rd', 'th'][min(n % 10, 4)]
    if 11 <= (n % 100) <= 13:
        suffix = 'th'
    return str(n) + suffix


ctx = Context('numbers')
ctx.set_rules({
    'number <n>': lambda m: insert(str(m['n'])),
    'ordinal <n>': lambda m: insert(ordinal(m['n'])),
})
