from osprey.voice import Context, insert

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

vocab_list = [
    'backtrace',
    'bifurcate',
    'bitwise',
    'callable',
    'cardioid',
    'changelog',
    'checkout',
    'committer',
    'config',
    'deallocate',
    'deallocated',
    'deallocating',
    'delimiter',
    'delimiters',
    'delineator',
    'delineators',
    'Erlang',
    'Flatpak',
    'formatter',
    'formatters',
    'GitLab',
    'Gitter',
    'glob',
    'grep',
    'homeserver',
    'Kaldi',
    'kinesis',
    'lints',
    'Neovim',
    'nondeterminism',
    'nondeterministic',
    'ordinal',
    'prepend',
    'readd',
    'README',
    'refactor',
    'reinstantiate',
    'struct',
    'structs',
    'subcommand',
    'subcommands',
    'subprocess',
    'subprocesses',
    'sudo',
    'tendinitis',
    'tendinosis',
    'tendon',
    'tendons',
    'tig',
    'todo',
    'Todoist',
    'TypeScript',
    'Unicode',
    'uninstalling',
    'vi',
    'vim',
    'vocab',

    'CLI',
    'GNU',
    'GUI',
    'POSIX',
    'TOML',
    'TUI',
    'YAML',

    'omegalul',
    'pog',
    'pogchamp',
    'poggers',
]

vocab_map = {
    'e v dev': 'evdev',
    'free b s d': 'FreeBSD',
    'h top': 'htop',
    'j peg': 'JPEG',
    'j query': 'jQuery',
    'j son': 'JSON',
    'mac o s': 'macOS',
    'monka s': 'monkaS',
    'net b s d': 'NetBSD',
    'n vim': 'nvim',
    'open b s d': 'OpenBSD',
    'pip x': 'pipx',
    'p s util': 'psutil',
    'u input': 'uinput',
    'u t f 8': 'UTF-8',
    'x eighty six': 'x86',
    'x eighty six sixty four': 'x86_64',
}
vocab_map.update({word: word for word in vocab_list})
vocab_map.update({' '.join(word.lower()): word for word in acronyms_spell_out_list})

subcommands = {
    'all caps': lambda s: s.upper(),
    'lower': lambda s: s.lower(),
    'upper': lambda s: s.capitalize(),
}


def vocab(m):
    vocab = vocab_map[m['vocab']]
    if m['subcommands']:
        subcommand = subcommands[m['subcommands']]
        vocab = subcommand(vocab)
    if 'dotted' in m['transcript']:
        vocab = '.'.join(vocab) + '.'
    insert(vocab)


ctx = Context('vocab')
ctx.set_commands({
    'vocab [<subcommands>] [dotted] <vocab>': vocab,
})
ctx.set_choices({
    'vocab': vocab_map.keys(),
    'subcommands': subcommands.keys(),
})
