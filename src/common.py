def normalise_keys(dict):
    normalised_dict = {}
    for k, v in dict.items():
        for cmd in k.split('|'):
            normalised_dict[cmd] = v
    return normalised_dict


digit_homophones = normalise_keys({
    "won": "1",
    "to|too": "2",
    "for|fore|form": "4",
    "ate": "8",
})
