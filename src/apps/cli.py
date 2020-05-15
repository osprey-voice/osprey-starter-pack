from osprey.voice import Context, insert

cli_map = {
    'parent': '../',
    'move': 'mv ',
    'remove': 'rm ',
    'cd': 'cd ',
    'link': 'ln ',
    'symbolic link': 'ln -s',
    'list': 'ls ',
    'copy': 'cp ',
    'flag': '--',
}

ctx = Context('cli')
ctx.set_commands({
    '<cli>': lambda m: insert(cli_map[m['cli']]),
})
ctx.set_choices({
    'cli': cli_map,
})
