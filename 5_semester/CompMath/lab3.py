import math

ACCURACY = 0.0001


def primitive_iteration(x, a=3, b=6, c=-24):
    return a * (x ** 2) + b * x - c


def primitive_root_finding(a=3, b=6, c=-24):
    x = []
    sign = 1
    for i in range(2):
        x.append((-1 * b + sign * math.sqrt(b ** 2 - 4 * a * c)) / (2 * a))
        sign *= -1
    return x


def iteration(x):
    pass


print(str(primitive_root_finding()))
