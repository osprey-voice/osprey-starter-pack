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
    "left": "Left",
    "right": "Right",
    "up": "Up",
    "down": "Down",
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
    # NOTE:  This should only contain symbols that do not require any modifier
    # keys to press on a standard US keyboard layout. Commands for keys that do
    # require modifiers (e.g. ``"caret": "^"`) should belong in
    # ``text/symbol.py``.
    "tick|back tick|backtick": "`",
    "comma|,": ",",
    "dot|period|.": ".",
    "semicolon|semi": ";",
    "quote|single quote": "'",
    "square|L square|left square|left square bracket": "[",
    "R square|right square|right square bracket": "]",
    "slash|forward slash": "/",
    "backslash": "\\",
    "minus|dash": "-",
    "equals": "=",

    # simple
    "(question [mark] | questo)": "?",
    "plus": "+",
    "tilde": "~",
    "(bang | exclamation point | clamor)": "!",
    "(dollar [sign] | dolly)": "$",
    "(downscore | crunder)": "_",
    "colon": ":",
    "(lparen | [left] paren | precorp )": "(",
    "(rparen | are paren | right paren | precose)": ")",
    "(brace | left brace | kirksorp)": "{",
    "(rbrace | are brace | right brace | kirkos)": "}",
    "(angle | left angle | less than)": "<",
    "(rangle | are angle | right angle | greater than)": ">",
    "(star | asterisk)": "*",
    "(pound | hash [sign] | octo | number sign)": "#",
    "percent [sign]": "%",
    "caret": "^",
    "at sign": "@",
    "(and sign | ampersand | amper)": "&",
    "(pipe | spike)": "|",
    "(dubquote | double quote | quatches)": '"',
    # compound
    "mintwice": "--",
    "plustwice": "++",
    "minquall": "-=",
    "pluqual": "+=",
    "starqual": "*=",
    "triple quote": "'''",
    "triple tick": "```",
    "[forward] dubslash": "//",
    "coal twice": "::",
    "(dot dot | dotdot)": "..",
    "(ellipsis | dot dot dot | dotdotdot)": "...",
    # unnecessary: use repetition commands?
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

# separate arrow dictionary for combining with modifiers
arrows = {"left": "Left", "right": "Right", "up": "Up", "down": "Down"}

# map alnum and keys separately so engine gives priority to letter/number repeats
keymap = keys.copy()
keymap.update(alphabet)
keymap.update(digits)
keymap.update(arrows)


def get_modifiers(m):
    try:
        return [modifiers[mod] for mod in m["modifiers"]]
    except KeyError:
        return []


def get_keys(m):
    groups = [
        "keys",
        "arrows",
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
        press("-".join(mods + [keys[0]]))
        keys = keys[1:]
    for k in keys:
        press(k)


ctx = Context("basic_keys")
ctx.set_keymap({
    "(uppercase|upper|shift) {alphabet+}(lowercase|lower)?": uppercase_letters,
    "{modifiers*}{alphabet+}": press_keys,
    "{modifiers*}{digits+}": press_keys,
    "{modifiers*}{keys+}": press_keys,
    "(go|{modifiers+}) {arrows+}": press_keys,
    "number {digits+}(over)?": press_keys,
})
ctx.set_lists({
    "alphabet": alphabet.keys(),
    "digits": digits.keys(),
    "keys": keys.keys(),
    "arrows": arrows.keys(),
    "modifiers": modifiers.keys(),
    "keymap": keymap.keys(),
})
