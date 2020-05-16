from osprey.voice import Context, insert

cli_map = {
    'cd': 'cd ',
    'copy': 'cp ',
    'link': 'ln ',
    'list': 'ls ',
    'make dir': 'mkdir ',
    'move': 'mv ',
    'remove': 'rm ',
    'remove dir': 'rmdir ',
    'symbolic link': 'ln -s ',
    'word count': 'wc ',

    'force': '-f ',
    'recursive': '-r ',
    'verbose': '-v ',

    'flag': '--',
    'version': '--version',

    'parent': '../',
}

ctx = Context('cli')
ctx.set_commands({
    '<cli>': lambda m: insert(cli_map[m['cli']]),
})
ctx.set_choices({
    'cli': cli_map,
})
