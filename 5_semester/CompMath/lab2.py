import math
import my_error

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


def matrix_diagonal_division(array, mod=1):
    """
    Divides each line of the system by the corresponding diagonal element of the matrix, which later multiplies by mod
    :param array: array Source array
    :param mod: int Factor
    :return: array
    """
    if len(array) == 0 or len(array) != len(array[0]):
        return None
    for i in range(len(array)):
        value = array[i][i]
        array[i][i] *= mod
        for j in range(len(array[i])):
            array[i][j] /= value
    return array


def matrix_multiplication(first_matrix, second_matrix):
    third_matrix = []
    for i in range(len(first_matrix)):
        for j in range(len(second_matrix[0])):
            value = 0
            for k in range(len(second_matrix)):
                value += first_matrix[i][k] * second_matrix[k][j]
            #third_matrix[i][j] = value
            #print(str(value))
    return third_matrix


def iterations_number(norm_b, norm_c, r=0.01):
    try:
        if my_error.SubZeroError.check(norm_b, norm_c) == 0:
            raise my_error.SubZeroError(norm_b, norm_c)
    except my_error.SubZeroError as e:
        print(e.msg)
    else:
        number = math.log((r * (1 - norm_c)) / norm_b) / math.log(norm_c)
        if number // 2 > 0:
            return round(number) - 1
        else:
            return number


def matrix_reduction(array):
    if len(array) == 0 or len(array) != len(array[0]):
        return None
    for i in range(len(array)):
        array[i][i] = 0
    return array


test_array = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

test_array2 = [
    [10, -1, 4],
    [3, 10, -5],
    [-1, -3, 5]
]

a = [
    [-1, 1],
    [2, 0],
    [0, 3]
]

b = [
    [3, 1, 2],
    [0, -1, 4]
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
"""
print(norm_first(test_array))
print(norm_second(test_array))
print(norm_infinite(test_array))
"""
#print(matrix_diagonal_division(test_array))
#print(str(iterations_number(norm_second(b_array), norm_second(matrix_diagonal_division(a_array)))))
#print(str(iterations_number(1.2, 0.8)))
#print(matrix_diagonal_division(test_array2, 0))
print(matrix_multiplication(a, b))
