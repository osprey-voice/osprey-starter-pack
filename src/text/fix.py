from osprey.voice import Context, insert

fix_map = {
    'jason': 'json',
    'type script': 'TypeScript',
}

ctx = Context('fix')
ctx.set_rules({
    'fix <fix>': lambda m: insert(fix_map[m['fix']]),
})
ctx.set_lists({
    'fix': fix_map.keys(),
})
