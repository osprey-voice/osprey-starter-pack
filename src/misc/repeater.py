from osprey.voice import Context, repeat

digits = [str(n) for n in range(2, 100)]

ctx = Context("repeater")
ctx.set_rules({
    "repeat {digits}": lambda m: repeat(int(m["digits"][0]) - 1),
})
ctx.set_lists({
    "digits": digits,
})
