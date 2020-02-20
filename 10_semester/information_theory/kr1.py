from collections import Counter
from heapq import heappush, heappop, heapify
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


def entropy_count(filename: str, size=1, print_log=False) -> float:
    file_str = _string_prepare(filename)
    symbols = _get_symbols_array(file_str, size)

    unique_symbols, counts = np.unique(symbols, return_counts=True)

    p = counts / np.sum(counts)

    H = -np.sum(p * np.log2(p)) / size

    if print_log:
        print('for file {} get symbols: {}'.format(filename, unique_symbols))
        print('entropy of {}: {}'.format(filename, H))

    return H


def redundancy_count(filename: str, size=1, print_log=False) -> float:
    file_str = _string_prepare(filename)
    symbols = _get_symbols_array(file_str, size)

    _, counts = np.unique(symbols, return_counts=True)

    H = entropy_count(filename, size)
    H_max = np.log2(len(counts))
    r = 1. - (H / H_max)

    if print_log:
        print('redundancy of {}: {}'.format(filename, r))

    return r


def huffman(file_str: str, print_log=False) -> dict:
    symbols = Counter(file_str)
    heap = [[wt, [sym, ""]] for sym, wt in symbols.items()]
    heapify(heap)
    while len(heap) > 1:
        lo = heappop(heap)
        hi = heappop(heap)
        for pair in lo[1:]:
            pair[1] = '0' + pair[1]
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]
        heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])

    huff = dict(sorted(heappop(heap)[1:], key=lambda p: (len(p[-1]), p), reverse=True))

    if print_log:
        print('huffman codes: {}'.format(huff))

    return huff


def redundancy_encoding_count(_dict: dict, entropy: float, print_log=False) -> float:
    lengths_array = np.array([len(i) for i in _dict.values()])
    length, counts = np.unique(lengths_array, return_counts=True)
    p = counts / np.sum(counts) * length
    p_sum = np.sum(p)
    r = p_sum - entropy

    if print_log:
        print('average code length: {}, redundancy: {}'.format(p_sum, r))

    return r


def huffman_encode_file(filename: str, file_prefix='encoded_', huff=None, print_log=False) -> str:
    file_str = _string_prepare(filename)

    if huff is None:
        huff = huffman(file_str, print_log=print_log)

    if [i for i in ['0', '1'] if i in huff]:
        if '0' in huff:
            file_str = file_str.replace('0', 'O')
            huff['O'] = huff.pop('0')
        if '1' in huff:
            file_str = file_str.replace('1', 'I')
            huff['I'] = huff.pop('1')

    for symbol in huff:
        file_str = file_str.replace(symbol, huff[symbol])

    with open(file_prefix + filename, 'w+') as f:
        f.write(file_str)

    return file_prefix + filename


if __name__ == '__main__':
    # generate_file_1(FILENAME_1)
    # generate_file_2(FILENAME_2)

    str_len = 1
    print_log = True

    for filename in [FILENAME_1, FILENAME_2, FILENAME_3]:
        entropy = entropy_count(filename, size=str_len, print_log=print_log)
        redundancy_count(filename, size=str_len, print_log=print_log)
        huff = huffman(_string_prepare(filename), print_log=print_log)
        new_filename = huffman_encode_file(filename, huff=huff, print_log=print_log)
        redundancy_encoding_count(huff, entropy, print_log=print_log)
        entropy_count(new_filename, size=str_len, print_log=print_log)
        redundancy_count(new_filename, size=str_len, print_log=print_log)
        if print_log:
            print()
