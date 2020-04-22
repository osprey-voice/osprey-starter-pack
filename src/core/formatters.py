import string
import re

from osprey.voice import Context, insert, press, repeat, undo_insert


def uppercase_i(s):
    return re.sub(r'\bi\b', 'I', s)


ctx = Context('formatters')
ctx.set_rules({
    # 'upper <word>': lambda m: insert(m['word'].capitalize()),
    # 'lower <word>': lambda m: insert(m['word'].lower()),
    # 'word <word>': lambda m: insert(m['word']),

    'phrase <phrase>': lambda m: insert(uppercase_i(m['phrase'])),
    'title <phrase>': lambda m: insert(string.capwords(m['phrase'])),
    'sentence <phrase>': lambda m: insert(uppercase_i(m['phrase'].capitalize())),
    'all caps <phrase>': lambda m: insert(m['phrase'].upper()),

    'undo insert': lambda m: undo_insert(),
})
