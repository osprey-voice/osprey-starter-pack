import string

from osprey.voice import Context, insert

ctx = Context('formatters')
ctx.set_rules({
    # 'upper <word>': lambda m: insert(m['word'].capitalize()),
    # 'lower <word>': lambda m: insert(m['word'].lower()),
    # 'word <word>': lambda m: insert(m['word']),
    'phrase <phrase>': lambda m: insert(m['phrase']),
    'title <phrase>': lambda m: insert(string.capwords(m['phrase'])),
    'sentence <phrase>': lambda m: insert(m['phrase'].capitalize()),
    'all caps <phrase>': lambda m: insert(m['phrase'].upper()),
})
