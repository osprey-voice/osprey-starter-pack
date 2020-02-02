from osprey.voice import Context, insert, preferred_phrases

ctx = Context("formatters")
ctx.set_rules({
    "upper {word}": lambda m: insert(m['word'][0].capitalize()),
    "lower {word}": lambda m: insert(m['word'][0].lower()),
    "word {word}": lambda m: insert(m['word'][0]),
    "(phrase|praise) {phrase}": lambda m: insert(m['phrase'][0]),
    "sentence {phrase}": lambda m: insert(m['phrase'][0][0].upper() + m['phrase'][0][1:]),
})

preferred_phrases.update({"upper", "lower", "word", "phrase", "sentence"})
