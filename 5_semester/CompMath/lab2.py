N = 2
C = 0.01 * N


def listsum(num_list, mod=1):
    """
    Sum of elements in the series
    :param num_list: array
    :param mod: int
    :return: int|real
    """
    the_sum = 0
    for i in num_list:
        the_sum += i ** mod
    return the_sum


def norm_infinite(array):
    norm = []
    for i in range(len(array)):
        norm.insert(i, listsum(array[i]))
    return max(norm)


def norm_first(array):
    array_t = list(zip(*array))
    return norm_infinite(array_t)


def norm_second(array):
    norm = []
    for i in range(len(array)):
        norm.append(listsum(array[i], 2))
    return round(listsum(norm) ** (1/2), 4)

test_array = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

a_array = [
    [0.95 + C, 0.26 + C, (-0.17) + C, 0.27 + C],
    [(-0.15) + C, 1.26 + C, 0.36 + C, 0.42 + C],
    [0.26 + C, (-0.54) + C, (-1.76) + C, 0.31 + C],
    [(-0.44) + C, 0.29 + C, (-0.78) + C, (-1.78) + C]
]

b_array = [
    [2.48], [(-3.16)], [1.52], [(-1.29)]
]

x_array = []

#print(my_array)
for i in range(len(a_array)):
    for j in range(len(a_array[i])):
        a_array[i][j] = round(a_array[i][j], 4)
#print(my_array)

print(norm_first(test_array))
print(norm_second(test_array))
print(norm_infinite(test_array))
