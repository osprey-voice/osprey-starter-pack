from osprey.voice import Context, repeat

from ..common import normalise_keys, words_to_digits

number_regex = r'(\d+|{})'.format('|'.join(list(words_to_digits.keys())))


def convert_number(s):
    if s in words_to_digits:
        s = words_to_digits[s]
    return int(s)


ctx = Context('repeater')
ctx.set_rules({
    'repeat {number}': lambda m: repeat(convert_number(m['number'][0]) - 1),
})
ctx.set_regexes({
    'number': number_regex,
})