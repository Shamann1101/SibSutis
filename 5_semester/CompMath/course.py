import math

H = 0.1
ACCURACY = 0.0001


def method_runge_kutta(x, y, h=H):
    k1 = runge_kutta_k1(x, y)
    k2 = runge_kutta_k2(x, y, k1, h)
    k3 = runge_kutta_k3(x, y, k2, h)
    k4 = runge_kutta_k4(x, y, k3, h)
    return y + (h / 6) * (k1 + 2 * k2 + 2 * k3 + k4)


def func_y(x, y):
    return (math.cos(y) / (4 + x)) + y


def runge_kutta_k1(x, y):
    return func_y(x, y)


def runge_kutta_k2(x, y, k1, h=H):
    return func_y(x + h / 2, y + h / 2 * k1)


def runge_kutta_k3(x, y, k2, h=H):
    return func_y(x + h / 2, y + h / 2 * k2)


def runge_kutta_k4(x, y, k3, h=H):
    return func_y(x + h, y + h * k3)


def runge_kutta_table(x, y, a, b, h):
    n = int((b - a) / h)
    keys = list()
    values = list()
    result = dict()
    result[x] = y
    keys.append(x)
    values.append(y)
    for i in range(1, n + 1):
        x += h
        y = method_runge_kutta(x, values[i - 1], h)
        keys.append(x)
        values.append(y)
        result[x] = y
    return result


def integrate_func(y):
    return y ** 2


def simpsons_formula(a, b, h=H):
    n = int((b - a) / h)
    result = a + b
    x = a + h
    i = 1
    for j in range(1, n):
        result += (3 + i) * integrate_func(x)
        x += h
        i *= -1
    result *= h / 3
    return result


#print(method_runge_kutta(0.1, 0, 0.1))
print(runge_kutta_table(0, 0.1, 0, 1, 0.5))
#print(runge_kutta_table(0.1, 0, 0, 1, 0.5 / 2))
print(simpsons_formula(0, 1))
#http://www.wolframalpha.com/input/?i=y%27%3D(cos(y))+%2F+(4+%2B+x)+%2B+y,+y(0)%3D0.1,+h%3D0.5,+using+Runge-Kutta+method,+from+0+to+1
