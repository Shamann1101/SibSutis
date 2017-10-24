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
    table = dict()
    i = float(c)
    while i <= C + 30 * h:
        table[i] = func(i)
        i = round(i + h, 4)
    return table


def find_nearest(table, x):
    value = None
    next_elem = True
    for elem in table.keys():
        if elem >= x and next_elem == True:
            value = [elem, table[elem]]
            next_elem = False
        elif elem >= x and next_elem == False:
            value.append(elem)
            print(value)
            return value
        

def interpolation(x, y, nearest_pair, h=H):
    q = (x - nearest_pair[0]) / h
    inter = nearest_pair[1] + q * (nearest_pair[2] - nearest_pair[1])
    return round(inter, 4)


def iter_table_create(c=C, h=H):
    table = dict()
    for n in range(30):
        x = func_i(n)
        table[x] = [interpolation(x, func(x), find_nearest(table_create(), x), h), func(x)]
    return table


print(table_create())
print(iter_table_create())
