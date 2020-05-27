from osprey.voice import Context, insert

acronyms_list = [
    'Ajax',
    'ASCII',
    'CLI',
    'GNU',
    'GUI',
    'NASA',
    'NATO',
    'POSIX',
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
    'GTK',
    'HD',
    'HTML',
    'HTTP',
    'HTTPS',
    'IDE',
    'IO',
    'IP',
    'IT',
    'LGPL',
    'MIT',
    'MP3',
    'npm',
    'npx',
    'NTP',
    'OS',
    'PDF',
    'PhD',
    'PHP',
    'PR',
    'QT',
    'RSI',
    'SQL',
    'SSD',
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
    'YAML',
]

acronyms_map = {
    'j son': 'JSON',
}
acronyms_map.update({word: word for word in acronyms_list})
acronyms_map.update({' '.join(word.lower()): word for word in acronyms_spell_out_list})

subcommands = {
    'all caps': lambda s: s.upper(),
    'lower': lambda s: s.lower(),
    'upper': lambda s: s.capitalize(),
}


def acronyms(m):
    acronym = acronyms_map[m['acronyms']]
    if m['subcommands']:
        subcommand = subcommands[m['subcommands']]
        acronym = subcommand(acronym)
    if 'dotted' in m['transcript']:
        acronym = '.'.join(acronym) + '.'
    insert(acronym)


ctx = Context('acronyms')
ctx.set_commands({
    'acronym [<subcommands>] [dotted] <acronyms>': acronyms,
})
ctx.set_choices({
    'acronyms': acronyms_map.keys(),
    'subcommands': subcommands.keys(),
})
