from osprey.voice import Context, repeat

ctx = Context('repeater')
ctx.set_rules({
    'repeat <n>': lambda m: repeat(m['n'] - 1),
})
