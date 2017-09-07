import math
import my_error

N = 2
C = 0.01 * N


def list_sum(num_list, mod=1):
    """
    Sum of elements in the series
    :param num_list: array
    :param mod: int The degree to which members of the series
    :return: int|real
    """
    the_sum = 0
    for i in num_list:
        the_sum += math.fabs(i) ** mod
    return the_sum


def norm_infinite(array):
    norm = []
    for i in range(len(array)):
        norm.insert(i, list_sum(array[i]))
    return max(norm)


def norm_first(array):
    array_t = list(zip(*array))
    return norm_infinite(array_t)


def norm_second(array):
    norm = []
    for i in range(len(array)):
        norm.append(list_sum(array[i], 2))
    return round(math.sqrt(list_sum(norm)), 4)


def get_matrix_diagonal_values(matrix):
    try:
        if len(matrix) == 0:
            raise ValueError
    except ValueError:
        print("The matrix can not be empty")
    else:
        new_matrix = [0] * len(matrix)
        for i in range(len(matrix)):
            new_matrix[i] = [0]
            new_matrix[i][0] = matrix[i][i]
        return new_matrix


def set_matrix_diagonal_values(matrix, value=0):
    try:
        if len(matrix) == 0:
            raise ValueError
    except ValueError:
        print("The matrix can not be empty")
    else:
        new_matrix = matrix
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                new_matrix[i][i] = value
        return new_matrix


def matrix_multiplication(first_matrix, second_matrix):
    try:
        if len(first_matrix[0]) != len(second_matrix):
            raise Exception
    except Exception:
        print("The dimension of the matrices is not suitable for multiplication")
    else:
        new_matrix = [0] * len(first_matrix)
        for i in range(len(first_matrix)):
            new_matrix[i] = [0] * len(second_matrix[0])
            for j in range(len(second_matrix[0])):
                value = 0
                for k in range(len(second_matrix)):
                    value += first_matrix[i][k] * second_matrix[k][j]
                new_matrix[i][j] = value
        return new_matrix


def matrix_multiplication_by_number(first_matrix, value, division=0):
    try:
        if type(value) != list and type(value) != int:
            raise TypeError
    except TypeError:
        print("Value must be list or int type")
    else:
        new_matrix = [0] * len(first_matrix)

        if type(value) == list:
            if (len(first_matrix)) == 1:
                first_matrix = list(zip(*first_matrix))
            for i in range(len(first_matrix)):
                new_matrix[i] = [0] * len(first_matrix[i])
                for j in range(len(first_matrix[i])):
                    if division == 0:
                        new_matrix[i][j] = first_matrix[i][j] * value[i][0]
                    else:
                        new_matrix[i][j] = first_matrix[i][j] / value[i][0]

        elif type(value) == int:
            for i in range(len(first_matrix)):
                new_matrix[i] = [0] * len(first_matrix[i])
                for j in range(len(first_matrix[i])):
                    if division == 0:
                        new_matrix[i][j] = first_matrix[i][j] * value
                    else:
                        new_matrix[i][j] = first_matrix[i][j] / value

        return new_matrix


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

test_array3 = [
    [1], [0], [6]
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

c_array = matrix_multiplication_by_number(test_array2, get_matrix_diagonal_values(test_array2), 1)
c_array = set_matrix_diagonal_values(c_array)
c_norm = norm_infinite(c_array)
b_array = matrix_multiplication_by_number(test_array3, get_matrix_diagonal_values(test_array2), 1)
b_norm = norm_infinite(b_array)
n = iterations_number(b_norm, c_norm)

print(c_array)
print(str(c_norm))
print(b_array)
print(str(b_norm))
print(str(n))
