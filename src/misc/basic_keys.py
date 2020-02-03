import string

from osprey.voice import Context, press, insert, preferred_phrases

from ..common import normalise_keys, digit_homophones


talon_alphabet_words = "air bat cap drum each fine gust harp sit jury crunch look made near odd pit quench red sun trap urge vest whale plex yank zip"
twoshea_alphabet_words = talon_alphabet_words.replace('drum', 'dip').replace(
    'fine', 'far').replace('gust', 'gone').replace('made', 'mad')
default_alphabet_words = talon_alphabet_words.replace('gust', 'gone')

alphabet_words = default_alphabet_words

alphabet = dict(zip(alphabet_words.split(), string.ascii_lowercase))

function_keys = {f"F{i}": f"F{i}" for i in range(1, 13)}

misc_keys = normalise_keys({
    "left|go left": "Left",
    "right|go right": "Right",
    "up|go up": "Up",
    "down|go down": "Down",
    "caps lock": "CapsLock",
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

punctuation = normalise_keys({
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

key_homophones = normalise_keys({
    "are|there|their|they're": "a",
    "find": "f",
    "con|gun": "g",
    "jewelry": "j",
    "book|work": "l",
    "on": "o",
    "son": "s",
    "best": "v",
    "well|will": "w",
    "inc|ink": "y",

    "airspace": ["a", "Space"],
    "forgone|foregone": ["4", "g"],
    "armpit": ["o", "p"],
    "concap": ["g", "c"],

    "outlook": "Alt l",
})

keys = {}
keys.update(function_keys)
keys.update(misc_keys)
keys.update(punctuation)
keys.update(alphabet)
keys.update(digits)
keys.update(key_homophones)
keys.update(digit_homophones)

modifiers = normalise_keys({
    "command": "Cmd",
    "control|troll": "Ctrl",
    "shift": "Shift",
    "alt|option": "Alt",
})

modifier_homophones = normalise_keys({
    "old|ulta|oat|oats": "Alt",
})

modifiers_with_homophones = {}
modifiers_with_homophones.update(modifiers)
modifiers_with_homophones.update(modifier_homophones)


def press_key_with_modifiers(m):
    mods = [modifiers_with_homophones[mod.lower()] for mod in m['modifiers']]
    key = keys[m['keys'][0].lower()]
    if isinstance(key, str):
        press(" ".join(mods + [key]))
    elif isinstance(key, list):
        press(" ".join(mods + [key[0]]))
        for k in key[1:]:
            press(k)


def press_keys(m):
    for key in m['keys']:
        mapping = keys[key.lower()]
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
    "modifiers": modifiers_with_homophones.keys(),
})

preferred_phrases.update(set(alphabet.keys()))
preferred_phrases.update(set(misc_keys.keys()))
preferred_phrases.update(set(punctuation.keys()))
preferred_phrases.update(set(function_keys.keys()))
preferred_phrases.update(set(digits.keys()))

preferred_phrases.update(set(modifiers.keys()))
