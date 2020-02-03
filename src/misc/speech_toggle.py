from osprey.voice import Context, ContextGroup, default_context_group, preferred_phrases

toggle_group = ContextGroup("toggle")
toggle = Context("toggle", group=toggle_group)
toggle.set_rules({
    "sleep": lambda: default_context_group.disable(),
    "wake": lambda: default_context_group.enable(),
})

preferred_phrases.update({"sleep", "wake"})
