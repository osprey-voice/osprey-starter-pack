import string

from osprey.voice import Context, press, insert, preferred_phrases

from ..common import normalise_keys, digit_homophones, words_to_digits


alphabet_words = [
    'art',
    'big',
    'cat',
    'dark',
    'eat',
    'food',
    'good',
    'hook',
    'sit',
    'juke',
    'kite',
    'look',
    'made',
    'near',
    'or',
    'poke',
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
    "underscore|under score|under": "_",
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
    "ampersand": "&",
    "star|asterisk": "*",
    "paren|open paren|left paren": "(",
    "close paren|right paren": ")",
})

digits = {str(i): str(i) for i in range(10)}

key_homophones = normalise_keys({
    "cats|cap|caps": "c",
    "eats": "e",
    "goods": "g",
    "set|it|suit|suits|city|sits": "i",
    "book|work": "l",
    "maid": "m",
    "polk": "p",
    "read": "r",
    "son": "s",
    "trapp|trump": "t",
    "purge": "u",
    "weak": "w",

    "write": "Right",
    "d1": "Down",
    "pack": "Backspace",
    "keep": "Escape",
    "picture up|peach up": "PageUp",
    "page d1": "PageDown",
    "hunter|center": "Enter",

    "carrot": "^",
    "thick|tech|tic|pic": "`",
    "tilda": "~",
    "but": ".",
    "quotes": "'",
    "colin": ":",

    "backpack": ["Backspace", "Backspace"],
})

keys = {}
keys.update(function_keys)
keys.update(misc_keys)
keys.update(punctuation)
keys.update(alphabet)
keys.update(digits)
keys.update(key_homophones)
keys.update(digit_homophones)
keys.update(words_to_digits)

modifiers = normalise_keys({
    "command": "Cmd",
    "control|troll": "Ctrl",
    "shift": "Shift",
    "option": "Alt",
})

modifier_homophones = normalise_keys({
})

modifiers_with_homophones = {}
modifiers_with_homophones.update(modifiers)
modifiers_with_homophones.update(modifier_homophones)


def press_key(m):
    mods = [modifiers_with_homophones[mod.lower()] for mod in m['modifiers']] if 'modifiers' in m else []
    key = keys[m['keys'][0].lower()]
    if isinstance(key, str):
        press(" ".join(mods + [key]))
    elif isinstance(key, list):
        press(" ".join(mods + [key[0]]))
        for k in key[1:]:
            press(k)


def press_punctuation(m):
    mods = [modifiers_with_homophones[mod.lower()] for mod in m['modifiers']] if 'modifiers' in m else []
    key = m['punctuation'][0]
    press(" ".join(mods + [key]))


ctx = Context("basic_keys")
ctx.set_rules({
    "{modifiers*}{keys}": press_key,
    "{modifiers*}{punctuation}": press_punctuation,
})
ctx.set_lists({
    "keys": keys.keys(),
    "modifiers": modifiers_with_homophones.keys(),
})
ctx.set_regexes({
    "punctuation": '[' + ''.join(string.punctuation) + ']',
})

preferred_phrases.update(set(alphabet.keys()))
preferred_phrases.update(set(misc_keys.keys()))
preferred_phrases.update(set(punctuation.keys()))
preferred_phrases.update(set(function_keys.keys()))
preferred_phrases.update(set(digits.keys()))

preferred_phrases.update(set(modifiers.keys()))
