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


def table_create(c=C, h=H):
    """
    Creates a table of values of the function with the calculated step h on the interval [c, c + 30h]
    :param c:
    :param h:
    :return:
    """
    table = dict()
    i = float(c)
    while i <= C + 30 * h:
        table[i] = func(i)
        i = round(i + h, 4)
    table = take_nearest(table)
    return table


def find_nearest(table, x):
    """
    Looks for the nearest value of an argument and a function
    :param table:
    :param x:
    :return:
    """
    keys = list(table.keys())
    for i in range(len(keys) - 1):
        if x >= keys[i] and x <= keys[i + 1]:
            return keys[i]
    return keys[len(keys) - 1]


def take_nearest(table):
    """
    Adds the values of neighboring elements to the dictionary
    :param table:
    :return:
    """
    new_table = dict()
    keys = list(table.keys())
    values = list(table.values())
    for i in range(len(table)):
        if i == 0:
            left = values[0]
            right = values[i + 1]
        elif i == len(table) - 1:
            left = values[i - 1]
            right = values[len(table) - 1]
        else:
            left = values[i - 1]
            right = values[i + 1]
        new_table[keys[i]] = [left, values[i], right]
    return new_table


def interpolation(x, x_left, y_left, y_right, h=H):
    """
    Linear interpolation
    :param x:
    :param nearest_pair:
    :param h:
    :return:
    """
    q = (x - x_left) / h
    inter = y_left + q * (y_right - y_left)
    return round(inter, 4)


def iter_table_create(table, h=H):
    """
    Creates a table of values of the interpolation
    :param h:
    :return:
    """
    new_table = dict()
    for n in range(30):
        x = func_i(n)
        nearest = find_nearest(table, x)
        new_table[x] = [interpolation(x, nearest, table[nearest][1], table[nearest][2]), func(x)]
    return new_table


table = table_create()
print(table)
print(iter_table_create(table))
