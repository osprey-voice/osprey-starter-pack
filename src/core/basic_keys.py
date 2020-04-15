import string

from osprey.voice import Context, press, insert

from ..common import normalise_keys, words_to_digits


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

function_keys = {f'F{i}': f'F{i}' for i in range(1, 13)}

misc_keys = normalise_keys({
    'left': 'Left',
    'right': 'Right',
    'up': 'Up',
    'down': 'Down',
    'caps lock': 'CapsLock',
    'back|backspace': 'Backspace',
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
    'square|open square|left square|bracket|open bracket|left bracket': '[',
    'close square|right square|close bracket|right bracket': ']',
    'backslash': '\\',

    # shift required
    'tilde': '~',
    'underscore|under score|under': '_',
    'plus': '+',
    'angle|open angle|left angle|less than': '<',
    'close angle|right angle|greater than': '>',
    'question|question mark': '?',
    'colon': ':',
    'double quote|double quotes': '"',
    'brace|open brace|left brace|curly|open curly|left curly': '{',
    'close brace|right brace|close curly|right curly': '}',
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
    'paren|open paren|left paren': '(',
    'close paren|right paren': ')',
})

digits = {str(i): str(i) for i in range(10)}

keys = {}
keys.update(function_keys)
keys.update(misc_keys)
keys.update(punctuation)
keys.update(alphabet)
keys.update(digits)
keys.update(words_to_digits)

modifiers = normalise_keys({
    'command': 'Cmd',
    'control|troll': 'Ctrl',
    'shift': 'Shift',
    'alt': 'Alt',
})


def press_key(m):
    mods = [modifiers[mod.lower()] for mod in m['modifiers']] if 'modifiers' in m else []
    key = keys[m['keys'][0].lower()]
    if isinstance(key, str):
        press(' '.join(mods + [key]))
    elif isinstance(key, list):
        press(' '.join(mods + [key[0]]))
        for k in key[1:]:
            press(k)


def press_punctuation(m):
    mods = [modifiers[mod.lower()] for mod in m['modifiers']] if 'modifiers' in m else []
    key = m['punctuation'][0]
    press(' '.join(mods + [key]))


ctx = Context('basic_keys')
ctx.set_rules({
    '{modifiers*}{keys}': press_key,
    '{modifiers*}{punctuation}': press_punctuation,
})
ctx.set_lists({
    'keys': keys.keys(),
    'modifiers': modifiers.keys(),
})
ctx.set_regexes({
    'punctuation': '[' + ''.join(string.punctuation) + ']',
})
