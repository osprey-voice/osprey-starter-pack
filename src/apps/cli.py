from osprey.voice import Context, insert

cli_map = {
    'cd': 'cd ',
    'copy': 'cp ',
    'link': 'ln ',
    'list': 'ls ',
    'make dir': 'mkdir ',
    'move': 'mv ',
    'p grep': 'pgrep ',
    'p kill': 'pkill ',
    'remove': 'rm ',
    'remove dir': 'rmdir ',
    'symbolic link': 'ln -s ',

    'all': '-a ',
    'force': '-f ',
    'interactive': '-i ',
    'long': '-l ',
    'recursive': '-r ',
    'silent': '-s ',
    'verbose': '-v ',

    'flag': '--',
    'help': '--help',
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
