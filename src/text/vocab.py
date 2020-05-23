from osprey.voice import Context, insert

vocab_list = [
    'backtrace',
    'bifurcate',
    'bitwise',
    'callable',
    'cardioid',
    'changelog',
    'committer',
    'config',
    'delineator',
    'delineators',
    'Erlang',
    'Flatpak',
    'formatter',
    'formatters',
    'git',
    'GitLab',
    'gitter',
    'grep',
    'json',
    'Kaldi',
    'kinesis',
    'lints',
    'Neovim',
    'nondeterminism',
    'nondeterministic',
    'prepend',
    'readd',
    'README',
    'refactor',
    'reinstantiate',
    'struct',
    'structs',
    'subprocess',
    'subprocesses',
    'sudo',
    'tendon',
    'tendons',
    'tendonitis',
    'tig',
    'TypeScript',
    'uninstalling',
    'Vim',
    'vocab',
]

vocab_map = {
    'j query': 'jQuery',
    'p s util': 'psutil',
}
vocab_map.update({word: word for word in vocab_list})

ctx = Context('vocab')
ctx.set_commands({
    'vocab <vocab>': lambda m: insert(vocab_map[m['vocab']]),
    'vocab upper <vocab>': lambda m: insert(vocab_map[m['vocab']].capitalize()),
    'vocab lower <vocab>': lambda m: insert(vocab_map[m['vocab']].lower()),
    'vocab all caps <vocab>': lambda m: insert(vocab_map[m['vocab']].upper()),
})
ctx.set_choices({
    'vocab': vocab_map.keys(),
})
