from osprey.voice import Context, insert

acronyms_list = [
    'Ajax',
    'API',
    'CLI',
    'CPU',
    'GUI',
    'PHP',
    'TUI',
    'XML',
]

acronyms_map = {
    'a b i': 'ABI',
    'a o e': 'AoE',
    'a u r': 'AUR',
    'c c r': 'CCR',
    'Jason': 'JSON',
}
acronyms_map.update({word: word for word in acronyms_list})

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
