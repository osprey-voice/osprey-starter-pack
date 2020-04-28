from osprey.voice import Context, insert, press


def code_block(m):
    insert('```')
    press('Enter')
    press('Enter')
    insert('```')
    press('Up')


ctx = Context('markdown')
ctx.set_rules({
    'check box': lambda m: insert('- [ ] '),
    'code block': code_block,
})
