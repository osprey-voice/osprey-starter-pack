import string

from osprey.voice import Context, press, insert

from ..utils import normalize_keys


alphabet_words = [
    'art',
    'bit',
    'cat',
    'dip',
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
    'zap',
]

alphabet = dict(zip(alphabet_words, string.ascii_lowercase))

one_to_twelve = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve']
function_keys = {f'function {word}': f'F{i}' for i, word in enumerate(one_to_twelve)}

misc_keys = normalize_keys({
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

punctuation = normalize_keys({
    # no shift required
    'tick|back tick|backtick': '`',
    'minus|dash|hyphen|negative': '-',
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

zero_to_nine = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
digits = {word: str(i) for i, word in enumerate(zero_to_nine)}

keys = {}
keys.update(function_keys)
keys.update(misc_keys)
keys.update(punctuation)
keys.update(alphabet)
keys.update(digits)

modifiers = normalize_keys({
    'control|troll|command': 'Ctrl',
    'shift': 'Shift',
    'alt|option': 'Alt',
})


def press_key(m):
    mods = [modifiers[mod] for mod in m['modifiers']]
    key = keys[m['keys']]
    press(' '.join(mods + [key]))


ctx = Context('basic_keys')
ctx.set_commands({
    '<modifiers>* <keys>': press_key,
})
ctx.set_choices({
    'keys': keys.keys(),
    'modifiers': modifiers.keys(),
})
