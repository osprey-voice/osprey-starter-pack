from osprey.voice import Context, ContextGroup, default_context_group

ctx_group = ContextGroup('speech_toggle')

ctx = Context('speech_toggle', group=ctx_group)
ctx.set_commands({
    'osprey sleep': lambda m: default_context_group.disable(),
    'osprey wake': lambda m: default_context_group.enable(),
})
