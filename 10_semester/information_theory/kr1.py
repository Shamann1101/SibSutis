from os import stat
from random import random

import numpy as np

FILENAME_1 = 'file_1.txt'
FILENAME_2 = 'file_2.txt'
FILENAME_3 = 'file_3.txt'
_FILE_SIZE = 10_000
_EXCLUDE_SYMBOLS = ('.', ',', '!', '?', '-', '^', ':', ';', '(', ')', '"', '\'', '\n', '\t')


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
    x = random()
    vector = _get_result_vector(_dict)
    for pair in vector:
        if x < pair[0]:
            return pair[1]


def generate_file_1(title='file_1.txt', length=_FILE_SIZE):
    with open(title, 'w+') as f:
        letters = ('a', 'b', 'c', 'd')
        chance = 1. / len(letters)

        letters_dict = dict().fromkeys(letters, chance)

        while stat(title).st_size < length:
            f.write(_get_random_symbol(letters_dict))


def generate_file_2(title='file_2.txt', length=_FILE_SIZE):
    with open(title, 'w+') as f:
        letters = {
            'a': 0.51,
            'b': 0.13,
            'c': 0.08,
            'd': 0.28,
        }

        while stat(title).st_size < length:
            f.write(_get_random_symbol(letters))


def _string_prepare(filename: str) -> str:
    with open(filename, 'r') as f:
        file_str = f.read().lower()

    for symbol in _EXCLUDE_SYMBOLS:
        file_str = file_str.replace(symbol, '+')

    return file_str


def _get_symbols_array(file_str: str, size: int) -> np.ndarray:
    symbols_list = []

    for i in range(len(file_str) - size + 1):
        symbols_list.append(file_str[i:i + size])

    symbols = np.array(symbols_list)

    return symbols


def entropy_count(filename: str, size=1, print_symbols=False) -> float:
    file_str = _string_prepare(filename)
    symbols = _get_symbols_array(file_str, size)

    unique_symbols, counts = np.unique(symbols, return_counts=True)

    if print_symbols:
        print('for file {} get symbols: {}'.format(filename, unique_symbols))

    p = counts / np.sum(counts)

    H = -np.sum(p * np.log2(p)) / size

    return H


def redundancy_count(filename: str, size=1) -> float:
    file_str = _string_prepare(filename)
    symbols = _get_symbols_array(file_str, size)

    _, counts = np.unique(symbols, return_counts=True)

    H = entropy_count(filename, size)
    H_max = np.log2(len(counts))
    r = 1. - (H / H_max)

    return r


def _get_alphabet(filename: str, size=1) -> dict:
    file_str = _string_prepare(filename)
    symbols = _get_symbols_array(file_str, size)

    unique_symbols, counts = np.unique(symbols, return_counts=True)
    summation = np.sum(counts)

    _dict = {unique_symbols[i]: counts[i] / summation for i in range(len(unique_symbols))}

    return _dict


def hoffman(_in: dict or list):
    if type(_in) == dict:
        _in = list(_in.values())
        _in.sort(reverse=True)
    elif type(_in) != list:
        raise TypeError
    print('in', _in)
    if len(_in) > 2:
        summation = np.sum(_in[-2:])
        print('summation', summation)
        _in[-2] = summation
        _in.pop()
        _in.sort(reverse=True)
        index = _in.index(summation)
        print('in', _in)
        hoffman(_in)
        print('index', index)
    return _in  # FIXME


if __name__ == '__main__':
    # generate_file_1(FILENAME_1)
    # generate_file_2(FILENAME_2)
    #
    # print('entropy of file_1.txt', entropy_count(FILENAME_1))
    # print('redundancy of file_1.txt', redundancy_count(FILENAME_1))
    # print('entropy of file_2.txt', entropy_count(FILENAME_2))
    # print('redundancy of file_2.txt', redundancy_count(FILENAME_2))
    # print('entropy of file_3.txt', entropy_count(FILENAME_3))
    # print('redundancy of file_3.txt', redundancy_count(FILENAME_3))

    # print(_get_alphabet(FILENAME_1))
    hoffman([0.36, 0.18, 0.18, 0.12, 0.09, 0.07])
