import string

from osprey.voice import Context, press, insert

from ..utils import normalise_keys


talon_alphabet_words = "air bat cap drum each fine gust harp sit jury crunch look made near odd pit quench red sun trap urge vest whale plex yank zip"
twoshea_alphabet_words = talon_alphabet_words.replace('drum', 'dip').replace(
    'fine', 'far').replace('gust', 'gone').replace('made', 'mad')
default_alphabet_words = talon_alphabet_words.replace('gust', 'gone')

alphabet_keys = default_alphabet_words.split()

alphabet = dict(zip(alphabet_keys, string.ascii_lowercase))
alphabet.update({"are": "a"})

f_keys = {f"F{i}": f"F{i}" for i in range(1, 13)}

simple_keys = normalise_keys({
    "left|go left": "Left",
    "right|go right": "Right",
    "up|go up": "Up",
    "down|go down": "Down",
    "backspace": "Backspace",
    "delete|forward delete": "Delete",
    "space": "Space",
    "tab": "Tab",
    "enter": "Enter",
    "escape": "Escape",
    "home": "Home",
    "end": "End",
    "page up": "PageUp",
    "page down": "PageDown",
})

symbols = normalise_keys({
    # no shift required
    "tick|back tick|backtick": "`",
    "minus|dash|hyphen": "-",
    "equals": "=",
    "comma": ",",
    "dot|period": ".",
    "slash|forward slash": "/",
    "semicolon|semi": ";",
    "quote|single quote|apostrophe": "'",
    "square|l square|open square|bracket|l bracket|open bracket": "[",
    "r square|are square|close square|r bracket|are bracket|close bracket": "]",
    "backslash": "\\",

    # shift required
    "tilde": "~",
    "underscore|under score": "_",
    "plus": "+",
    "angle|l angle|open angle|less than": "<",
    "r angle|are angle|close angle|greater than": ">",
    "question|question mark": "?",
    "colon": ":",
    "double quote": '"',
    "brace|l brace|open brace": "{",
    "r brace|are brace|close brace": "}",
    "pipe|bar": "|",

    # above numbers
    "bang|exclamation|exclamation point": "!",
    "at sign": "@",
    "pound|pound sign|hash|hash sign|hashtag|hash tag|number sign": "#",
    "dollar|dollar sign": "$",
    "percent|percent sign": "%",
    "caret": "^",
    "ampersand|amper": "&",
    "star|asterisk": "*",
    "paren|l paren|open paren": "(",
    "r paren|are paren|close paren": ")",
})

digits = {str(i): str(i) for i in range(10)}
digits.update({"to": "2", "too": "2", "for": "4"})

keys = {}
keys.update(f_keys)
keys.update(simple_keys)
keys.update(symbols)
keys.update(alphabet)
keys.update(digits)
keys.update({"airspace": ["a", "Space"]})

modifiers = normalise_keys({
    "command": "Cmd",
    "control|troll": "Ctrl",
    "shift": "Shift",
    "alt|option": "Alt",
})


def press_key_with_modifiers(m):
    mods = [modifiers[mod] for mod in m['modifiers']]
    key = keys[m['keys'][0]]
    if isinstance(key, str):
        press(" ".join(mods + [key]))
    elif isinstance(key, list):
        press(" ".join(mods + [key[0]]))
        for k in key[1:]:
            press(k)


def press_keys(m):
    for key in m['keys']:
        mapping = keys[key]
        if isinstance(mapping, str):
            press(mapping)
        elif isinstance(mapping, list):
            for k in mapping:
                press(k)


ctx = Context("basic_keys")
ctx.set_rules({
    "{modifiers+}{keys}": press_key_with_modifiers,
    "{keys+}": press_keys,
})
ctx.set_lists({
    "keys": keys.keys(),
    "modifiers": modifiers.keys(),
})
