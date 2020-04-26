from osprey.voice import Context, insert

fix_list = [
    'add',
    'and',
    'desk',
]

ctx = Context('fix')
ctx.set_rules({
    'fix <fix>': lambda m: insert(m['fix']),
})
ctx.set_lists({
    'fix': fix_list,
})
