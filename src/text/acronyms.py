from osprey.voice import Context, insert

acronyms_map = {
    'a b i': 'ABI',
    'a o e': 'AoE',
    'a u r': 'AUR',
    'Ajax': 'Ajax',
    'API': 'API',
    'c c r': 'CCR',
    'CLI': 'CLI',
    'CPU': 'CPU',
    'GUI': 'GUI',
    'Jason': 'JSON',
    'PHP': 'PHP',
    'TUI': 'TUI',
    'XML': 'XML',
}

ctx = Context('acronyms')
ctx.set_commands({
    'acronym <acronyms>': lambda m: insert(acronyms_map[m['acronyms']]),
    'acronym upper <acronyms>': lambda m: insert(acronyms_map[m['acronyms']].capitalize()),
    'acronym lower <acronyms>': lambda m: insert(acronyms_map[m['acronyms']].lower()),
    'acronym all caps <acronyms>': lambda m: insert(acronyms_map[m['acronyms']].upper()),
})
ctx.set_choices({
    'acronyms': acronyms_map.keys(),
})
