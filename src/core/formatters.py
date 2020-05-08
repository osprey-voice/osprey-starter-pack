import re
import string

from osprey.voice import Context, insert, press, repeat, undo_insert


def uppercase_i(s):
    return re.sub(r'\bi\b', 'I', s)


def camel_case(m):
    words = m['phrase'].split(' ')
    formatted_words = [word if i == 0 else word.capitalize() for i, word in enumerate(words)]
    joined = ''.join(formatted_words)
    insert(joined)


ctx = Context('formatters')
ctx.set_commands({
    # 'word <word>': lambda m: insert(m['word']),
    # 'upper <word>': lambda m: insert(m['word'].capitalize()),
    # 'lower <word>': lambda m: insert(m['word'].lower()),

    'phrase <phrase>': lambda m: insert(uppercase_i(m['phrase'])),
    'sentence <phrase>': lambda m: insert(uppercase_i(m['phrase'].capitalize())),

    'all caps <phrase>': lambda m: insert(m['phrase'].upper()),
    'camel <phrase>': camel_case,
    'kebab <phrase>': lambda m: insert(m['phrase'].replace(' ', '-')),
    'kebab title <phrase>': lambda m: insert(string.capwords(m['phrase']).replace(' ', '-')),
    'smash <phrase>': lambda m: insert(m['phrase'].replace(' ', '')),
    'smash title <phrase>': lambda m: insert(string.capwords(m['phrase']).replace(' ', '')),
    'snake <phrase>': lambda m: insert(m['phrase'].replace(' ', '_')),
    'snake all caps <phrase>': lambda m: insert(m['phrase'].replace(' ', '_').upper()),
    'title <phrase>': lambda m: insert(string.capwords(m['phrase'])),

    'undo insert': lambda m: undo_insert(),
})
