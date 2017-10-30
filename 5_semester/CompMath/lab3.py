import math

ACCURACY = 0.0001
INFINITY = 100000


def ndigits(x=ACCURACY):
    """"
    Returns accuracy of values in decimal places
    """
    n = 0
    while x != 1:
        x *= 10
        n += 1
    return n


def ab_range(a, b):
    """
    Returns the interval between two numbers
    :param a:
    :param b:
    :return:
    """
    i = 1
    if (a * b) > 0:
        i = -1
    return math.fabs(math.fabs(a) + i * math.fabs(b))


def primitive_iteration(x, a=1, b=3, c=-24, d=-10, accuracy=ACCURACY):
    """
    Returns the value of an equation of the third degree with given coefficients
    :param x:
    :param a:
    :param b:
    :param c:
    :param d:
    :param accuracy:
    :return:
    """
    if type(accuracy) != int:
        accuracy = ndigits(accuracy)
    return round(a * (x ** 3) + b * (x ** 2) + c * x + d, accuracy)


def primitive_root_finding(a=3, b=6, c=-24):
    """
    Returns the roots of the second-degree equation with given coefficients
    :param a:
    :param b:
    :param c:
    :return:
    """
    x = []
    sign = 1
    for i in range(2):
        x.append((-1 * b + sign * math.sqrt(b ** 2 - 4 * a * c)) / (2 * a))
        sign *= -1
    x.sort()
    return x


def interval_finding(value, start=(-1)*INFINITY, stop=INFINITY):
    """
    Returns list with interval dots
    :param value:
    :param start:
    :param stop:
    :return:
    """
    row = list()
    row.append(start)
    if type(value) == list or type(value) == tuple:
        if type(value) == tuple:
            value = list(value)
        row.extend(value)
    else:
        row.append(value)
    row.append(stop)
    row.sort()
    return row


def iterations_number(a, b, accuracy=ACCURACY):
    """
    Returns number of iterations
    :param a:
    :param b:
    :param accuracy:
    :return:
    """
    return round(math.log2((b - a) / accuracy))


def iteration(a, b, all_iterations_number=0, iteration_number=0, accuracy=ACCURACY):
    """
    Returns the interval on which the actual root is located
    :param a:
    :param b:
    :param all_iterations_number:
    :param iteration_number:
    :param accuracy:
    :return:
    """
    if all_iterations_number == 0:
        all_iterations_number = iterations_number(a, b, accuracy)
    if type(accuracy) != int:
        accuracy = ndigits(accuracy)
    c = round((a + b) / 2, accuracy)
    r = ab_range(a, b)
    if r > ACCURACY and iteration_number < all_iterations_number:
        if primitive_iteration(a) * primitive_iteration(c) < 0:
            b = c
        elif primitive_iteration(b) * primitive_iteration(c) < 0:
            a = c
        iteration_number += 1
        return iteration(a, b, all_iterations_number, iteration_number)
    else:
        return [a, b]


def real_root_finding(interval):
    """
    Returns all of the intervals on which the actual roots is located
    :param interval:
    :return:
    """
    root = list()
    for i in range(len(interval) - 1):
        root.insert(i, iteration(interval[i], interval[i+1]))
    return root


print(real_root_finding(interval_finding(primitive_root_finding())))
