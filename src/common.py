def normalise_keys(dict):
    normalised_dict = {}
    for k, v in dict.items():
        for cmd in k.split('|'):
            normalised_dict[cmd] = v
    return normalised_dict


digit_homophones = normalise_keys({
    'won': '1',
    'to|too': '2',
    'for|fore|form': '4',
    'ate': '8',
})

digit_words = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
words_to_digits = {digit_words[i]: str(i) for i in range(10)}
