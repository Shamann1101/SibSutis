import threading
from fast_enum import FastEnum
import random

ALPHABET = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "g", "k", "l ", "m", "n", "o", "p", "q", "r", "s", "t", "u",
            "v", "w", "x", "y", "z", "A", "B", "C", "D", "E ", "F", "G", "H", "I", "G", "K", "L", "M", "N", "O", "P",
            "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]


mutex = threading.Lock()


class AccessTypes(metaclass=FastEnum):
    READ = 'r'
    WRITE = 'w'


class ParallelProcess:
    created_process = 0
    file_name = 'datasets/input.txt'

    def __init__(self, _type: AccessTypes = AccessTypes.READ, _priority: int = 1):
        self._id = self.created_process + 1
        self._access_type = _type
        self._priority = _priority
        self._l_bound = 0
        self._h_bound = 0
        self._value = ''
        self._count_buffer = 0
        print(f'Create process, process id = {self._id}')
        self.created_process += 1

    def __del__(self):
        self.created_process -= 1

    # def _convert_type_to_str(self):
    #     return self._access_type.name
    #
    # def _convert_str_to_type(self, access_type: str):
    #     if AccessTypes.READ

    @property
    def id(self):
        return self._id

    @property
    def access_type(self):
        return self._access_type

    @property
    def priority(self):
        return self._priority

    @property
    def l_bound(self):
        return self._l_bound

    @property
    def h_bound(self):
        return self._h_bound

    @access_type.setter
    def access_type(self, value: AccessTypes):
        self._access_type = value

    @priority.setter
    def priority(self, value: int):
        self._priority = value

    @l_bound.setter
    def l_bound(self, value: int):
        self._l_bound = value

    @h_bound.setter
    def h_bound(self, value: int):
        self._h_bound = value

    def show(self):
        print(f'Process id = {self._id}, type = {self._access_type.name}, priority = {self._priority}\n' +
              f'Lbound = {self._l_bound}, Hbound = {self._h_bound}')

    def show_value(self):
        print(f'Process id = {self._id}, type = {self._access_type.name}' +
              f'countBuffer = {self._count_buffer}\n' +
              f'Value = {self._value}')

    def show_id(self):
        print(f'Process id = {self._id}, type = {self._access_type.name}')

    def read(self):
        if self._access_type == AccessTypes.READ:
            with open(self.file_name, 'r') as f:
                print(f.read())

    def write(self):
        if self._access_type == AccessTypes.WRITE:
            with open(self.file_name, 'w') as f:
                f.write(random.choice(ALPHABET))


if __name__ == '__main__':
    pass
