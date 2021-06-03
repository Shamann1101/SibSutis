import helpers
from lab1 import elias_gamma
from lab2 import MTF


class BurrowsWheeler:
    EOS = "\0"

    def __init__(self):
        self._index = -1

    @property
    def index(self) -> int:
        return self._index

    def transform(self, s: list) -> list:
        # assert self.EOS not in s, "Input string cannot contain null character (%s)" % self.EOS

        rotations = [s[i:] + s[:i] for i in range(len(s))]

        table = sorted(rotations)

        last_column = [row[-1] for row in table]

        # r = ''.join(last_column)

        self._index = table.index(s)

        return last_column

    def inverse(self, s: list) -> str:
        table = [''] * len(s)

        for i in range(len(s)):
            prepended = [s[i].decode("utf-8") + table[i] for i in range(len(s))]

            table = sorted(prepended)

        s = table[self._index]

        return s


def _main():
    generated_file = __file__.split('.')[0] + '_generated.txt'
    helpers.generate_file(generated_file)
    for file_name in [__file__, generated_file, 'text.txt']:
        byte_list = helpers.get_byte_list_from_file(file_name)

        bwt = BurrowsWheeler()

        mtf = MTF(byte_list)

        cipher = mtf.encode(byte_list)
        elias_cipher = ''
        for char in cipher:
            elias_cipher += elias_gamma(int(char))

        helpers.write_bin_string_to_file(file_name.split('.')[0] + '_raw.txt', elias_cipher)
        # print(f'elias_cipher: {elias_cipher}')

        transform = bwt.transform(byte_list)
        # print('Burrows-Wheeler Transform: ' + str(transform))
        cipher = mtf.encode(transform)
        # print(f'cipher: {cipher}')
        elias_cipher = ''
        for char in cipher:
            elias_cipher += elias_gamma(int(char))

        helpers.write_bin_string_to_file(file_name.split('.')[0] + '_bwt.txt', elias_cipher)

        # with open(file_name.split('.')[0] + '_decoded.txt', 'w') as f:
        #     f.write(bwt.inverse(mtf.decode(cipher)))


if __name__ == '__main__':
    _main()
