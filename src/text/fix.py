from osprey.voice import Context, insert

fix_list = [
    'add',
    'and',
    'desk',
]

ctx = Context('fix')
ctx.set_commands({
    'fix <fix>': lambda m: insert(m['fix']),
})
ctx.set_choices({
    'fix': fix_list,
})
