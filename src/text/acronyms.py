from osprey.voice import Context, insert

acronyms_list = [
    'CLI',
    'GNU',
    'GUI',
    'POSIX',
    'TOML',
    'TUI',
    'YAML',
]

acronyms_spell_out_list = [
    'ABI',
    'AGPL',
    'AI',
    'ATM',
    'AUR',
    'BSD',
    'CCR',
    'CI',
    'CSS',
    'GPL',
    'GPU',
    'GTK',
    'HTTPS',
    'IDE',
    'IT',
    'LGPL',
    'MP3',
    'npm',
    'npx',
    'NTP',
    'OS',
    'PhD',
    'PNG',
    'PR',
    'QT',
    'RSI',
    'SSD',
    'SSL',
    'SVG',
    'TLS',
    'UDP',
    'UN',
    'US',
    'USA',
]

acronyms_map = {
    'j peg': 'JPEG',
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
