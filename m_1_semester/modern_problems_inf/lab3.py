from lab2 import MTF
from lab1 import elias_gamma


class BurrowsWheeler:
    EOS = "\0"

    def __init__(self):
        self._index = -1

    @property
    def index(self):
        return self._index

    def transform(self, s):
        # assert self.EOS not in s, "Input string cannot contain null character (%s)" % self.EOS

        rotations = [s[i:] + s[:i] for i in range(len(s))]

        table = sorted(rotations)

        last_column = [row[-1] for row in table]

        r = ''.join(last_column)

        self._index = table.index(s)

        return r

    def inverse(self, s):
        table = [''] * len(s)

        for i in range(len(s)):
            prepended = [s[i] + table[i] for i in range(len(s))]

            table = sorted(prepended)

        s = table[self._index]

        return s


def encode_bwt(sequence):
    sequence += '\0'
    table = [sequence[index:] + sequence[:index] for index, _ in enumerate(sequence)]
    table.sort()
    bwt = [rotation[-1] for rotation in table]
    bwt = ''.join(bwt)

    return bwt


def decode_bwt(sequence):
    table = [col for col in sequence]
    for i in range(len(sequence) - 1):
        table.sort()
        table = [sequence[i] + table[i] for i in range(len(sequence))]

    return table[[row[-1] for row in table].index('\0')].replace('\0', '')


def _main():
    # message = input('Enter sequence: ')
    # message = open('../../10_semester/information_theory/file_3.txt', mode='r').read()
    message = open('lab3.py', mode='r').read()

    bwt = BurrowsWheeler()

    mtf = MTF()
    mtf.set_alphabet_from_message(message)

    cipher = mtf.encode(message)
    # print(f'cipher: {cipher}')
    elias_cipher = ''
    for char in cipher:
        elias_cipher += elias_gamma(int(char))
    with open('raw.txt', mode='w') as f:
        f.write(elias_cipher)
    # print(f'elias_cipher: {elias_cipher}')

    transform = bwt.transform(message)
    # print('Burrows-Wheeler Transform: ' + str(transform))
    cipher = mtf.encode(transform)
    # print(f'cipher: {cipher}')
    elias_cipher = ''
    for char in cipher:
        elias_cipher += elias_gamma(int(char))
    with open('bwt.txt', mode='w') as f:
        f.write(elias_cipher)
    # print(f'elias_cipher: {elias_cipher}')

    # inverse = bwt.inverse(transform)
    # print('Inverse Burrows-Wheeler Transform: ' + str(inverse))


if __name__ == '__main__':
    _main()
