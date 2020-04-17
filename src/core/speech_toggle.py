from osprey.voice import Context, ContextGroup, default_context_group

ctx_group = ContextGroup('toggle')

ctx = Context('toggle', group=ctx_group)
ctx.set_rules({
    'sleep': lambda m: default_context_group.disable(),
    'wake': lambda m: default_context_group.enable(),
})
