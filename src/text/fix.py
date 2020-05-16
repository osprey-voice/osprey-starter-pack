from osprey.voice import Context, insert

fix_list = [
    'add',
    'and',
    'desk',
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
