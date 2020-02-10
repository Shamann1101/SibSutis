import random
from os import stat


FILE_SIZE = 10_000


def _get_result_vector(_dict: dict) -> tuple:
    summation = 0.
    vector = []

    for symbol in _dict:
        summation += _dict[symbol]

    if summation > 1.:
        raise ValueError('Value over 1')

    x = 1. / summation
    shift = 0.

    for symbol in _dict:
        vector.append((_dict[symbol] * x + shift, symbol))
        shift += _dict[symbol] * x

    return tuple(vector)


def _get_random_symbol(_dict: dict) -> str:
    x = random.random()
    vector = _get_result_vector(_dict)
    for pair in vector:
        if x < pair[0]:
            return pair[1]


def generate_file_1(title='file_1.txt', length=FILE_SIZE):
    with open(title, 'w+') as f:
        letters = ('a', 'b', 'c')
        chance = 1. / len(letters)

        letters_dict = dict()
        letters_dict.fromkeys(letters)

        for letter in letters:
            letters_dict[letter] = chance

        while stat(title).st_size < length:
            f.write(_get_random_symbol(letters_dict))


def generate_file_2(title='file_2.txt', length=FILE_SIZE):
    with open(title, 'w+') as f:
        letters = {
            'a': 1 / 5,
            'b': 1 / 2,
            'c': 1 / 7,
        }

        while stat(title).st_size < length:
            f.write(_get_random_symbol(letters))


if __name__ == '__main__':
    generate_file_1()
    generate_file_2()
