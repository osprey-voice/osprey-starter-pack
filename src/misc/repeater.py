from osprey.voice import Context, repeat, preferred_phrases

from ..common import normalise_keys, digit_homophones

number_regex = r'(\d+|{})'.format('|'.join(digit_homophones.keys()))


def convert_number(s):
    if s in digit_homophones:
        s = digit_homophones[s]
    return int(s)


ctx = Context("repeater")
ctx.set_rules({
    "repeat {number}": lambda m: repeat(convert_number(m["number"][0]) - 1),
})
ctx.set_regexes({
    "number": number_regex,
})

preferred_phrases.update({"repeat"})
