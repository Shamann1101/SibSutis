from copy import copy

import helpers
from lab1 import elias_gamma


class MTF:
    def __init__(self, alphabet: list = None):
        self._alphabet = list(set(alphabet)) if alphabet else list()
        self.__cipher = list()

    @property
    def alphabet(self) -> list:
        return self._alphabet

    @alphabet.setter
    def alphabet(self, value: list):
        if len(value) == 0:
            raise ValueError('Alphabet is empty')
        self._alphabet = list(set(value))

    def set_alphabet_from_message(self, message: str):
        self._alphabet = list(set(list(message)))

    def encode(self, message: list, alphabet: list = None) -> list:
        if alphabet is None:
            alphabet = copy(self._alphabet)
            self.__cipher = list()
        for symbol in message:
            index = alphabet.index(symbol)
            self.__cipher.append(index.__str__())
            alphabet.insert(0, alphabet.pop(index))
        return self.__cipher

    def decode(self, message: list, alphabet: list = None) -> list:
        if alphabet is None:
            alphabet = copy(self._alphabet)
            self.__cipher = list()
        for symbol in message:
            char = alphabet[int(symbol)]
            self.__cipher.append(char)
            alphabet.insert(0, alphabet.pop(int(symbol)))
        return self.__cipher


def _main():
    input_file_name = __file__
    byte_list = helpers.get_byte_list_from_file(input_file_name)

    mtf = MTF(byte_list)
    cipher = mtf.encode(byte_list)
    # print(f'cipher: {cipher}')

    elias_cipher = ''
    for char in cipher:
        elias_cipher += elias_gamma(int(char))
    # print(f'elias_cipher: {elias_cipher}')

    helpers.write_bin_string_to_file(input_file_name.split('.')[0] + '_out.txt', elias_cipher)

    # string_list = [x.decode('utf-8') for x in mtf.decode(cipher)]
    # print('decoded:\n' + ''.join(string_list))


if __name__ == '__main__':
    _main()
