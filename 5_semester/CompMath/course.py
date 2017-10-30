import math

H = 0.1
ACCURACY = 0.0001
A = 0
B = 1


def ndigits(x=ACCURACY):
    """"
    Returns accuracy of values in decimal places
    """
    n = 0
    while x != 1:
        x *= 10
        n += 1
    return n


def method_runge_kutta(x, y, h=H, accuracy=ACCURACY):
    """
    The solution of the differential equation by the Runge-Kutta method of the fourth order
    """
    if type(accuracy) != int:
        accuracy = ndigits(accuracy)
    k1 = runge_kutta_k1(x, y)
    k2 = runge_kutta_k2(x, y, k1, h)
    k3 = runge_kutta_k3(x, y, k2, h)
    k4 = runge_kutta_k4(x, y, k3, h)
    return round(y + (h / 6) * (k1 + 2 * k2 + 2 * k3 + k4), accuracy + 1)


def func_y(x, y):
    """
    The differentiable function
    """
    return (math.cos(y) / (4 + x)) + y


def runge_kutta_k1(x, y):
    """
    Runge-Kutta coefficient k1
    """
    return func_y(x, y)


def runge_kutta_k2(x, y, k1, h=H):
    """
    Runge-Kutta coefficient k2
    """
    return func_y(x + h / 2, y + h / 2 * k1)


def runge_kutta_k3(x, y, k2, h=H):
    """
    Runge-Kutta coefficient k3
    """
    return func_y(x + h / 2, y + h / 2 * k2)


def runge_kutta_k4(x, y, k3, h=H):
    """
    Runge-Kutta coefficient k4
    """
    return func_y(x + h, y + h * k3)


def runge_kutta_table(x, y, a, b, h):
    """
    Creation of a dictionary with the results of the Runge-Kutta method
    """
    n = int((b - a) / h)
    keys = list()
    values = list()
    result = dict()
    result[x] = y
    keys.append(x)
    values.append(y)
    for i in range(1, n + 1):
        y = method_runge_kutta(x, values[i - 1], h)
        x += h
        keys.append(x)
        values.append(y)
        result[x] = y
    return result


def runge_kutta_table_iterate(x, y, a, b, h, accuracy=ACCURACY):
    """
    Iteration by the Runge-Kutta method to achieve the specified accuracy
    """
    table1 = runge_kutta_table(x, y, a, b, h)
    table2 = runge_kutta_table(x, y, a, b, h / 2)
    values = list(table1.keys())
    for value in values:
        if abs(table1[value] - table2[value]) > accuracy:
            return runge_kutta_table_iterate(x, y, a, b, h/2, accuracy)
    return table1


def find_nearest(table, x):
    """
    Looks for the nearest value of an argument and a function
    :param table:
    :param x:
    :return:
    """
    keys = list(table.keys())
    for i in range(len(keys) - 1):
        if x >= keys[i] and x < keys[i + 1]:
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


def interpolation(x, x_left, y_left, y_right, h=0.1):
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


def iter_table_create(table, a, b, h=0.1, accuracy=ACCURACY):
    """
    Creates a table of values of the interpolation
    :param h:
    :return:
    """
    accuracy = ndigits(accuracy)
    new_table = dict()
    for n in range(11):
        x = round(0.1 * n, accuracy)
        nearest = find_nearest(table, x)
        new_table[x] = interpolation(x, nearest, table[nearest][1], table[nearest][2], h)
    return new_table


def integrate_func(y):
    """
    Integrand function
    """
    return y ** 2


def simpsons_formula(table, h=H):
    """
    Computing the integral by the Simpson method
    """
    n = len(table)
    values = list(table.values())
    result = integrate_func(values[0]) + integrate_func(values[n - 1])
    i = 1
    for j in range(1, n-1):
        result += (3 + i) * integrate_func(values[j])
        i *= -1
    result *= h / 3
    return result


rk = runge_kutta_table_iterate(0, 0.1, A, B, 0.5)
rk = take_nearest(rk)
print(rk)
keys = list(rk.keys())
step = keys[1]
rt = iter_table_create(rk, A, B, step)
print(rt)
print(simpsons_formula(rt, 0.1))
