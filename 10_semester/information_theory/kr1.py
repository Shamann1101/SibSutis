import random
from os import stat

import numpy as np

FILE_SIZE = 10_000


def _get_result_vector(_dict: dict) -> tuple:
    summation = 0.
    vector = []

    for symbol in _dict:
        summation += _dict[symbol]

    if summation > 1.:
        raise ValueError('Value over 1')

    shift_coefficient = 1. / summation
    shift = 0.

    for symbol in _dict:
        vector.append((_dict[symbol] * shift_coefficient + shift, symbol))
        shift += _dict[symbol] * shift_coefficient

    return tuple(vector)


def _get_random_symbol(_dict: dict) -> str:
    x = random.random()
    vector = _get_result_vector(_dict)
    for pair in vector:
        if x < pair[0]:
            return pair[1]


def generate_file_1(title='file_1.txt', length=FILE_SIZE):
    with open(title, 'w+') as f:
        letters = ('a', 'b', 'c', 'd')
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
            'a': 0.51,
            'b': 0.13,
            'c': 0.08,
            'd': 0.28,
        }

        while stat(title).st_size < length:
            f.write(_get_random_symbol(letters))


def entropy_count(filename: str) -> float:
    symbols_list = []

    with open(filename, 'r') as f:
        while True:
            symbol = f.read(1)
            if not symbol:
                break
            symbols_list.append(symbol)

    symbols = np.array(symbols_list)

    _, counts = np.unique(symbols, return_counts=True)
    p = counts / np.sum(counts)

    H = -np.sum(p * np.log2(p))

    return H


if __name__ == '__main__':
    generate_file_1()
    generate_file_2()

    print(entropy_count('file_1.txt'))
    print(entropy_count('file_2.txt'))
