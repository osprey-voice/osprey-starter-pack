from osprey.voice import Context, insert

vocab_list = [
    'config',
    'Erlang',
    'formatter',
    'GitLab',
    'json',
    'Kaldi',
    'kinesis',
    'Neovim',
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
