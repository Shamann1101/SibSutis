import math

N = 2
C = N + 1
H = 0.006


def mod4(i):
    return i % 4


def func(x):
    """
    Outputs the value of the function with the calculated step
    :param x: float
    :return: float
    """
    return round(2 * C ** 3 * math.sin(x / C), 4)


def func_i(i):
    """
    Using linear interpolation, calculates the values of a function at a point
    :param i: int
    :return: float
    """
    return round(C + (i * H) + (mod4(i) + 1) / 5 * H, 4)


i = float(C)
while i <= C + 30 * H:
    print("x = " + str(i) + " func = " + str(func(i)))
    i = round(i + H, 4)


for n in range(30):
    x = func_i(n)
    print("x" + str(n) + " = " + str(x) + " func = " + str(func(x)))
