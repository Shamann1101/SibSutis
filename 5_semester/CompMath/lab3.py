import math

ACCURACY = 0.0001
INFINITY = 100000


def ndigits(x=ACCURACY):
    n = 0
    while x != 1:
        x *= 10
        n += 1
    return n


def is_positive(x):
    if x == math.fabs(x):
        return True
    else:
        return False


def ab_range(a, b):
    i = 1
    if (a * b) > 0:
        i = -1
    return math.fabs(math.fabs(a) + i * math.fabs(b))


def primitive_iteration(x, a=1, b=3, c=-24, d=-10, accuracy=ACCURACY):
    if type(accuracy) != int:
        accuracy = ndigits(accuracy)
    return round(a * (x ** 3) + b * (x ** 2) + c * x + d, accuracy)


def primitive_root_finding(a=3, b=6, c=-24):
    x = []
    sign = 1
    for i in range(2):
        x.append((-1 * b + sign * math.sqrt(b ** 2 - 4 * a * c)) / (2 * a))
        sign *= -1
    return x


def iterations_number(a, b, accuracy=ACCURACY):
    return round(math.log2((b - a) / accuracy))


def iteration(a, b, all_iterations_number=0, iteration_number=0, accuracy=ACCURACY):
    if all_iterations_number == 0:
        all_iterations_number = iterations_number(a, b, accuracy)
    if type(accuracy) != int:
        accuracy = ndigits(accuracy)
    c = round((a + b) / 2, accuracy)
    r = ab_range(a, b)
    if r > ACCURACY and iteration_number < all_iterations_number:
        #print(str(a) + " " + str(b))
        if primitive_iteration(a) * primitive_iteration(c) < 0:
            b = c
        elif primitive_iteration(b) * primitive_iteration(c) < 0:
            a = c
        iteration_number += 1
        iteration(a, b, all_iterations_number, iteration_number)
    else:
        print(str(a) + " " + str(b))
        return [a, b]


#print(iteration((-1) * INFINITY, -4))
#print(iteration(-4, 2))
print(iteration(2, INFINITY))
#print(iterations_number(2, INFINITY))
