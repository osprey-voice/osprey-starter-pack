from osprey.voice import Context, insert

vocab_list = [
    'cardioid',
    'changelog',
    'config',
    'Erlang',
    'formatter',
    'git',
    'GitLab',
    'gitter',
    'grep',
    'json',
    'Kaldi',
    'kinesis',
    'Neovim',
    'prepend',
    'readd',
    'refactor',
    'struct',
    'subprocess',
    'sudo',
    'tig',
    'TypeScript',
    'vim',
    'vocab',
]

ctx = Context('vocab')
ctx.set_commands({
    'vocab <vocab>': lambda m: insert(m['vocab']),
})
ctx.set_choices({
    'vocab': vocab_list,
})
