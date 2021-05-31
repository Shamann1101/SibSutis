from copy import copy

from lab1 import elias_gamma


class MTF:
    def __init__(self, alphabet: list = None):
        self._alphabet = list(set(alphabet)) if alphabet else list()
        self.__cipher = ''

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

    def encode(self, message: str, alphabet: list = None) -> str:
        if alphabet is None:
            alphabet = copy(self._alphabet)
            self.__cipher = ''
        for symbol in message:
            index = alphabet.index(symbol)
            self.__cipher += index.__str__()
            alphabet.insert(0, alphabet.pop(index))
        return self.__cipher

    def decode(self, message: str, alphabet: list = None) -> str:
        if alphabet is None:
            alphabet = copy(self._alphabet)
            self.__cipher = ''
        for symbol in message:
            char = alphabet[int(symbol)]
            self.__cipher += char
            alphabet.insert(0, alphabet.pop(int(symbol)))
        return self.__cipher


def _main():
    alphabet = ['a', 'b', 'c', 'd', 'e']
    message = 'baadaade'

    mtf = MTF(alphabet)
    cipher = mtf.encode(message)
    print(f'cipher: {cipher}')

    elias_cipher = ''
    for char in cipher:
        elias_cipher += elias_gamma(int(char))
    print(f'elias_cipher: {elias_cipher}')

    print('message: ' + mtf.decode(cipher))


if __name__ == '__main__':
    _main()
