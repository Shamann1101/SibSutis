import math

ACCURACY = 0.0001
N = 2
A = 0
B = 0.5


def func_x(x):
    return math.e ** math.sqrt(x) * (x - 1) * (x - 10) * (x - N - 1) * (x - 0.5)


def iterate(a = A, b = B, n = 0, accuracy=ACCURACY):
    if b - a <= accuracy:
        x = (a + b) / 2
        #print(n, x)
        return func_x(x)
    y = 0.618 * a + 0.382 * b
    z = 0.382 * a + 0.618 * b
    func_y = func_x(y)
    func_z = func_x(z)
    if func_y > func_z:
        func_z = func_y
        z = y
        y = 0.618 * a + 0.382 * b
        func_y = func_x(y)
        n += 1
        return iterate(a, z, n, accuracy)
    else:
        func_y = func_z
        y = z
        z = 0.382 * a + 0.618 * b
        func_z = func_x(z)
        n +=1
        return iterate(y, b, n, accuracy)


print(iterate())
