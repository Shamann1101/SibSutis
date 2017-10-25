import math

ACCURACY = 0.0001
N = 2
C = 3 * ((0.1 * (N + 1)) ** 3)
H = 0.1547


def ndigits(x=ACCURACY):
    """"
    Returns accuracy of values in decimal places
    """
    n = 0
    while x != 1:
        x *= 10
        n += 1
    return n


def table_func(x, c=C):
    """
    Calculates a function for compiling a table
    :param x:
    :param c:
    :return:
    """
    return (1 / c ** 2) * math.cos(c * x)


def table_func_create(c=C, h=H, accuracy=ACCURACY):
    """
    Fills the table with the values of the corresponding function
    :param c:
    :param h:
    :param accuracy:
    :return:
    """
    if type(accuracy) != int:
        accuracy = ndigits(accuracy)
    x = round(c - h, accuracy)
    table = dict()
    while x <= (c + 21 * h):
        table[x] = round(table_func(x, c), accuracy)
        x = round(x + h, accuracy)
    table = take_nearest(table)
    return table


def exact_formula(x, c=C, accuracy=ACCURACY):
    """
    The exact value of the derivative
    :param x:
    :param c:
    :param accuracy:
    :return:
    """
    if type(accuracy) != int:
        accuracy = ndigits(accuracy)
    return round(-1 * math.sin(c * x) / c, accuracy)


def approximate_formula(left, right, h=H, accuracy=ACCURACY):
    """
    The approximate value of the derivative
    :param left:
    :param right:
    :param h:
    :param accuracy:
    :return:
    """
    if type(accuracy) != int:
        accuracy = ndigits(accuracy)
    return round((right - left) / (2 * h), accuracy)


def approximate_formula_table(table, c=C, h=H, accuracy=ACCURACY):
    """
    Fills the table with the approximate values of the derivative
    :param table:
    :param c:
    :param h:
    :param accuracy:
    :return:
    """
    if type(accuracy) != int:
        accuracy = ndigits(accuracy)
    new_table = dict()
    for i in range(21):
        x = round(c + i * h, accuracy)
        nearest = find_nearest(table, x)
        new_table[x] = [approximate_formula(table[nearest][0], table[nearest][2]), exact_formula(x)]
    return new_table


def find_nearest(table, x):
    """
    Looks for the nearest value of an argument and a function
    :param table:
    :param x:
    :return:
    """
    for elem in table.keys():
        if elem >= x:
            return elem


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

print(table_func_create())
print(approximate_formula_table(table_func_create()))
