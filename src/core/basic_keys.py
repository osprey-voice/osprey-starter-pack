import string

from osprey.voice import Context, press, insert

from ..common import normalise_keys


alphabet_words = [
    'art',
    'bit',
    'cat',
    'dark',
    'each',
    'food',
    'good',
    'hike',
    'sit',
    'juke',
    'kite',
    'look',
    'mid',
    'near',
    'oak',
    'port',
    'quite',
    'red',
    'sun',
    'trap',
    'urge',
    'vest',
    'week',
    'plex',
    'york',
    'zip',
]

alphabet = dict(zip(alphabet_words, string.ascii_lowercase))

function_keys = {f'function {i}': f'F{i}' for i in range(1, 13)}

misc_keys = normalise_keys({
    'left': 'Left',
    'right': 'Right',
    'up': 'Up',
    'down': 'Down',
    'caps lock': 'CapsLock',
    'back|backspace|back space': 'Backspace',
    'delete': 'Delete',
    'space': 'Space',
    'tab': 'Tab',
    'enter': 'Enter',
    'cape|escape': 'Escape',
    'home': 'Home',
    'end': 'End',
    'page up': 'PageUp',
    'page down': 'PageDown',
})

punctuation = normalise_keys({
    # no shift required
    'tick|back tick|backtick': '`',
    'minus|dash|hyphen': '-',
    'equals|equal': '=',
    'comma': ',',
    'dot|period': '.',
    'slash|forward slash': '/',
    'semicolon|semi': ';',
    'quote|single quote|apostrophe': '\'',
    'square|open square|bracket|open bracket': '[',
    'close square|close bracket': ']',
    'backslash': '\\',

    # shift required
    'tilde': '~',
    'underscore|under score|under': '_',
    'plus': '+',
    'angle|open angle|less than': '<',
    'close angle|greater than': '>',
    'question|question mark': '?',
    'colon': ':',
    'double quote|double quotes': '"',
    'brace|open brace|curly|open curly': '{',
    'close brace|close curly': '}',
    'pipe|bar': '|',

    # above numbers
    'bang|exclamation|exclamation point': '!',
    'at sign': '@',
    'pound|pound sign|hash|hash sign|hashtag|hash tag|number sign': '#',
    'dollar|dollar sign': '$',
    'percent|percent sign': '%',
    'caret': '^',
    'ampersand': '&',
    'star|asterisk': '*',
    'paren|open paren': '(',
    'close paren': ')',
})

digits = {str(i): str(i) for i in range(10)}

keys = {}
keys.update(function_keys)
keys.update(misc_keys)
keys.update(punctuation)
keys.update(alphabet)
keys.update(digits)

modifiers = normalise_keys({
    'command': 'Cmd',
    'control|troll': 'Ctrl',
    'shift': 'Shift',
    'alt': 'Alt',
})


def press_key(m):
    mods = [modifiers[mod] for mod in m['modifiers']]
    key = keys[m['keys']]
    press(' '.join(mods + [key]))


ctx = Context('basic_keys')
ctx.set_rules({
    '<modifiers>* <keys>': press_key,
})
ctx.set_lists({
    'keys': keys.keys(),
    'modifiers': modifiers.keys(),
})
