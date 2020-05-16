from osprey.voice import Context, insert

symbols_map = {
    'arrow': '->',
    'wide arrow': '=>',
    'ellipsis': '...',
    'degree': '°',
}

ctx = Context('symbols')
ctx.set_commands({
    'symbol <symbols>': lambda m: insert(symbols_map[m['symbols']]),
})
ctx.set_choices({
    'symbols': symbols_map,
})
