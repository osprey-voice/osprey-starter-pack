import string

from osprey.voice import Context, insert, preferred_phrases

ctx = Context('formatters')
ctx.set_rules({
    'upper {word}': lambda m: insert(m['word'][0].capitalize()),
    'lower {word}': lambda m: insert(m['word'][0].lower()),
    'word {word}': lambda m: insert(m['word'][0]),
    '(phrase|praise|fries|freeze|prince) {phrase}': lambda m: insert(m['phrase'][0]),
    'title {phrase}': lambda m: insert(string.capwords(m['phrase'][0])),
    'sentence {phrase}': lambda m: insert(m['phrase'][0].capitalize()),
})
ctx.set_regexes({
    'word': r'\S+',
    'phrase': r'\S+(\s\S+)*',
})

preferred_phrases.update({'upper', 'lower', 'word', 'phrase', 'sentence'})
