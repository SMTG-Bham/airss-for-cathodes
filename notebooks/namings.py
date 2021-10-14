naming = {
    '8938': 'A',
    'f116': 'C',
    '32e9': 'B',
    'tavorite(MP)': 'Ta',
    '6304': 'D',
    'c062': 'E',
    'd823': 'F',
    '2389': 'G',
    'triplite_5': 'Tr-I',
    'triplite_0': 'Tr-II',
    'triplite_14': 'Tr-III'
}
def get_alias(label):
    for key, value in naming.items():
        if label.endswith(key):
            return value
    return None