from osprey.voice import Context, insert

ctx = Context('markdown')
ctx.set_rules({
    'check box': lambda m: insert('- [ ] '),
})
