from osprey.voice import Context, insert

ctx = Context("formatters")

ctx.set_keymap({
    "word {word}": lambda m: insert(m['word'][0]),
})
