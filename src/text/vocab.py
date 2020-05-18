from osprey.voice import Context, insert

vocab_list = [
    'backtrace',
    'callable',
    'cardioid',
    'changelog',
    'committer',
    'config',
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
    'prepend',
    'readd',
    'README',
    'refactor',
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

ctx = Context('vocab')
ctx.set_commands({
    'vocab <vocab>': lambda m: insert(m['vocab']),
    'vocab upper <vocab>': lambda m: insert(m['vocab'].capitalize()),
    'vocab lower <vocab>': lambda m: insert(m['vocab'].lower()),
    'vocab all caps <vocab>': lambda m: insert(m['vocab'].upper()),
})
ctx.set_choices({
    'vocab': vocab_list,
})
