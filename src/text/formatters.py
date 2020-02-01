from osprey.voice import Context, insert

ctx = Context("formatters")
ctx.set_rules({
    "word {word}": lambda m: insert(m['word'][0]),
    "(phrase|praise) {phrase}": lambda m: insert(m['phrase'][0]),
    "sentence {phrase}": lambda m: insert(m['phrase'][0][0].upper() + m['phrase'][0][1:]),
})
