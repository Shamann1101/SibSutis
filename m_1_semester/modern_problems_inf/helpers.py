import random

from bitstring import BitArray


def get_byte_list_from_file(file_name: str) -> list:
    byte_list = list()
    with open(file_name, mode='rb') as input_file:
        while True:
            byte = input_file.read(1)
            if not byte:
                break
            byte_list.append(byte)
    return byte_list


def generate_file(file_name: str, alphabet: list = None, size: int = 1024):
    if alphabet is None:
        alphabet = ['a', 'b', 'c']
    with open(file_name, mode='w') as output_file:
        output_file.write(''.join([random.choice(alphabet) for _ in range(size)]))


def write_bin_string_to_file(file_name: str, byte_str: str):
    if len(byte_str) % 8 != 0:
        byte_str += '0' * (8 - len(byte_str) % 8)

    mtf_array = BitArray(bin=byte_str)
    with open(file_name, mode='wb') as f:
        f.write(mtf_array.bytes)
