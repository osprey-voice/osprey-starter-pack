import string

from osprey.voice import Context, press, insert, preferred_phrases

from ..common import normalise_keys, digit_homophones


talon_alphabet_words = "air bat cap drum each fine gust harp sit jury crunch look made near odd pit quench red sun trap urge vest whale plex yank zip"
twoshea_alphabet_words = talon_alphabet_words \
    .replace('drum', 'dip') \
    .replace('fine', 'far') \
    .replace('gust', 'gone') \
    .replace('made', 'mad')
default_alphabet_words = talon_alphabet_words \
    .replace('air', 'art') \
    .replace('bat', 'big') \
    .replace('cap', 'cat') \
    .replace('drum', 'dip') \
    .replace('gust', 'gate') \
    .replace('crunch', 'kite') \
    .replace('fine', 'feed') \
    .replace('jury', 'joke') \
    .replace('whale', 'week')

alphabet_words = default_alphabet_words

alphabet = dict(zip(alphabet_words.split(), string.ascii_lowercase))

function_keys = {f"F{i}": f"F{i}" for i in range(1, 13)}

misc_keys = normalise_keys({
    "go left": "Left",
    "go right": "Right",
    "go up": "Up",
    "go down": "Down",
    "caps lock": "CapsLock",
    "back|backspace": "Backspace",
    "delete|forward delete": "Delete",
    "space": "Space",
    "tab": "Tab",
    "enter": "Enter",
    "cape|escape": "Escape",
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
    "square|open square|left square|bracket|open bracket|left bracket": "[",
    "close square|right square|close bracket|right bracket": "]",
    "backslash": "\\",

    # shift required
    "tilde": "~",
    "underscore|under score": "_",
    "plus": "+",
    "angle|open angle|left angle|less than": "<",
    "close angle|right angle|greater than": ">",
    "question|question mark": "?",
    "colon": ":",
    "double quote": '"',
    "brace|open brace|left brace|curly|open curly|left curly": "{",
    "close brace|right brace|close curly|right curly": "}",
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
    "paren|open paren|left paren": "(",
    "close paren|right paren": ")",
})

digits = {str(i): str(i) for i in range(10)}

key_homophones = normalise_keys({
    "cats": "c",
    "peach|itch|eat|eats|beach": "e",
    "gates": "g",
    "haarp": "h",
    "set|it|suit|suits|city|sits": "i",
    "stroke": "j",
    "book|work": "l",
    "maid": "m",
    "on|squad|pod": "o",
    "pits|pitt": "p",
    "read": "r",
    "son": "s",
    "trapp": "t",
    "purge": "u",
    "best": "v",
    "inc|ink": "y",

    "write": "Right",
    "d1": "Down",
    "pack": "Backspace",
    "keep": "Escape",
    "picture up": "PageUp",
    "page d1": "PageDown",

    "thick|tech|tic|pic": "`",
    "tilda": "~",
    "but": ".",
    "quotes": "'",

    "archery": ["a", "j"],
    "capcap": ["c", "c"],
    "airspace": ["a", "Space"],
    "armpit": ["o", "p"],
    "cromwell": ["d", "w"],

    "outlook": "Alt l",
    "altitude": "Alt 2",
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
    "old|ulta|oat|oats|oak": "Alt",
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


def press_key(m):
    key = keys[m['keys'][0].lower()]
    if isinstance(key, str):
        press(key)
    elif isinstance(key, list):
        for k in key:
            press(k)


ctx = Context("basic_keys")
ctx.set_rules({
    "{modifiers+}{keys}": press_key_with_modifiers,
    "{keys}": press_key,
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
