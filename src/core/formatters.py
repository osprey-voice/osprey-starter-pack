import re
import string

from osprey.voice import Context, insert, undo_insert


def uppercase_i(s):
    return re.sub(r'\bi\b', 'I', s)


def format(s, formatter):
    words = s.split(' ')
    formatted_text = [formatter(i, word) for i, word in enumerate(words)]
    joined = ''.join(formatted_text)
    return joined


def camel_case(m):
    phrase = m['phrase']
    formatter = lambda i, word: word if i == 0 else word.capitalize()
    formatted = format(phrase, formatter)
    insert(formatted)


formatters_map = {
    'all caps': lambda s: s.upper(),
    'title': lambda s: string.capwords(s),

    'kebab': lambda s: s.replace(' ', '-'),
    'smash': lambda s: s.replace(' ', ''),
    'snake': lambda s: s.replace(' ', '_'),
    'double under': lambda s: '__{}__'.format(s.replace(' ', '_')),
}


def formatters(m):
    phrase = m['phrase']
    if 'title' in m['formatters']:
        phrase = formatters_map['title'](phrase)
        m['formatters'].remove('title')
    for formatter in m['formatters']:
        phrase = formatters_map[formatter](phrase)
    insert(phrase)


ctx = Context('formatters')
ctx.set_commands({
    'word <word>': lambda m: insert(uppercase_i(m['word'])),
    'upper <word>': lambda m: insert(m['word'].capitalize()),
    'lower <word>': lambda m: insert(m['word'].lower()),

    'phrase <phrase>': lambda m: insert(uppercase_i(m['phrase'])),
    'sentence <phrase>': lambda m: insert(uppercase_i(m['phrase'].capitalize())),

    'camel <phrase>': camel_case,
    '<formatters>+ <phrase>': formatters,

    'undo insert': lambda m: undo_insert(),
})
ctx.set_choices({
    'formatters': formatters_map.keys(),
})
