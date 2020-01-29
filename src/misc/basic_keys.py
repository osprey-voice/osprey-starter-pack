import string

from osprey.voice import Context, press, insert

from ..utils import normalise_keys


talon_alphabet_words = "air bat cap drum each fine gust harp sit jury crunch look made near odd pit quench red sun trap urge vest whale plex yank zip"
twoshea_alphabet_words = talon_alphabet_words.replace('drum', 'dip').replace(
    'fine', 'far').replace('gust', 'gone').replace('made', 'mad')
default_alphabet_words = talon_alphabet_words.replace('gust', 'gone')

alphabet_keys = default_alphabet_words.split()

alphabet = dict(zip(alphabet_keys, string.ascii_lowercase))

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
    "tick|back tick|backtick": "`",
    "comma": ",",
    "dot|period": ".",
    "semicolon|semi": ";",
    "quote|single quote": "'",
    "square|l square|open square|bracket|l bracket|open bracket": "[",
    "r square|are square|close square|r bracket|are bracket|close bracket": "]",
    "slash|forward slash": "/",
    "backslash": "\\",
    "minus|dash": "-",
    "equals": "=",

    "question|question mark": "?",
    "plus": "+",
    "tilde": "~",
    "bang|exclamation|exclamation point": "!",
    "dollar|dollar sign": "$",
    "underscore|under score": "_",
    "colon": ":",
    "paren|l paren|open paren": "(",
    "r paren|are paren|close paren": ")",
    "brace|l brace|open brace": "{",
    "r brace|are brace|close brace": "}",
    "angle|l angle|open angle|less than": "<",
    "r angle|are angle|close angle|greater than": ">",
    "star|asterisk": "*",
    "pound|pound sign|hash|hash sign|hashtag|hash tag|number sign": "#",
    "percent|percent sign": "%",
    "caret": "^",
    "at sign": "@",
    "ampersand|amper": "&",
    "pipe|bar": "|",
    "double quote": '"',
})

modifiers = normalise_keys({
    "command": "Cmd",
    "control|troll": "Ctrl",
    "shift": "Shift",
    "alt|option": "Alt",
})

keys = {}
keys.update(f_keys)
keys.update(simple_keys)
keys.update(symbols)

digits = {str(i): str(i) for i in range(10)}
digits.update({"to": "2", "too": "2", "for": "4"})

# map alnum and keys separately so engine gives priority to letter/number repeats
keymap = keys.copy()
keymap.update(alphabet)
keymap.update(digits)


def get_modifiers(m):
    try:
        return [modifiers[mod] for mod in m["modifiers"]]
    except KeyError:
        return []


def get_keys(m):
    groups = [
        "keys",
        "digits",
        "alphabet",
        "keymap",
    ]
    for group in groups:
        try:
            return [keymap[k] for k in m[group]]
        except KeyError:
            pass
    return []


def uppercase_letters(m):
    insert("".join(get_keys(m)).upper())


def press_keys(m):
    mods = get_modifiers(m)
    keys = get_keys(m)

    if mods == ["shift"] and all(key in alphabet.values() for key in keys):
        return uppercase_letters(m)

    if mods:
        press(" ".join(mods + [keys[0]]))
        keys = keys[1:]
    for k in keys:
        press(k)


ctx = Context("basic_keys")
ctx.set_keymap({
    "(uppercase|upper|shift) {alphabet+}(lowercase|lower)?": uppercase_letters,
    "{modifiers*}{alphabet+}": press_keys,
    "{modifiers*}{digits+}": press_keys,
    "{modifiers*}{keys+}": press_keys,
    "number {digits+}(over)?": press_keys,
})
ctx.set_lists({
    "alphabet": alphabet.keys(),
    "digits": digits.keys(),
    "keys": keys.keys(),
    "modifiers": modifiers.keys(),
    "keymap": keymap.keys(),
})
