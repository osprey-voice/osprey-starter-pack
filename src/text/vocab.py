from osprey.voice import Context, insert

vocab_list = [
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
    'readd',
    'struct',
    'subprocess',
    'sudo',
    'tig',
    'TypeScript',
    'vim',
    'vocab',
]

ctx = Context('vocab')
ctx.set_rules({
    'vocab <vocab>': lambda m: insert(m['vocab']),
})
ctx.set_lists({
    'vocab': vocab_list,
})
