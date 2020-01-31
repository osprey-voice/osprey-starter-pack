from osprey.voice import Context, insert

ctx = Context("formatters")
ctx.set_rules({
    "word {word}": lambda m: insert(m['word'][0]),
    "phrase {phrase}": lambda m: insert(m['phrase'][0]),
})
