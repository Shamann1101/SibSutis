from math import log2, ceil
from typing import Callable


def _binary(x: int, l: int = 1) -> str:
    fmt = '{0:0%db}' % l
    return fmt.format(x)


def _unary(x: int) -> str:
    return x * '0' + '1'


def _elias_generic(method: Callable[[int], str], x: int) -> str:
    if x == 0:
        return '1'

    l = 1 + int(log2(x))
    a = x - 2 ** (int(log2(x)))

    k = int(log2(x))

    return method(l) + _binary(a, k)


def golomb(b: int, x: int) -> str:
    q = int(x / b)
    r = int(x % b)

    l = int(ceil(log2(b)))

    return _unary(q) + _binary(r, l)


def elias_gamma(x: int) -> str:
    return _elias_generic(_unary, x)


def elias_delta(x: int) -> str:
    return _elias_generic(elias_gamma, x)


def _main():
    print("Gamma-Code")
    for i in range(0, 10):
        print("%5d: %-10s " % (i, elias_gamma(i)))
    print("Delta-Code")
    for i in range(0, 10):
        print("%5d: %-10s " % (i, elias_delta(i)))


if __name__ == '__main__':
    _main()
