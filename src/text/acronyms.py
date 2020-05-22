from osprey.voice import Context, insert

acronyms_list = [
    'Ajax',
    'CLI',
    'GUI',
    'TUI',
]

acronyms_spell_out_list = [
    'ABI',
    'AGPL',
    'AI',
    'AoE',
    'API',
    'ATM',
    'AUR',
    'BSD',
    'CCR',
    'CD',
    'CI',
    'CPU',
    'CS',
    'CSS',
    'DB',
    'DVD',
    'EU',
    'GPL',
    'GPS',
    'GPU',
    'HTML',
    'HTTP',
    'HTTPS',
    'IO',
    'IP',
    'IT',
    'LGPL',
    'MIT',
    'MP3',
    'NTP',
    'OS',
    'PHP',
    'PR',
    'RSI',
    'SQL',
    'SSL',
    'SVG',
    'TCP',
    'TLS',
    'TV',
    'UDP',
    'UK',
    'UN',
    'US',
    'USA',
    'XML',
]

acronyms_map = {
    'Jason': 'JSON',
}
acronyms_map.update({word: word for word in acronyms_list})
acronyms_map.update({' '.join(word.lower()): word for word in acronyms_spell_out_list})

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
