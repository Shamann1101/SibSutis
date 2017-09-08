import math
import my_error

N = 2
C = 0.01 * N
ACCURACY = 0.0001


def list_sum(num_list, mod=1):
    """
    Sum of elements in the series
    :param num_list: list
    :param mod: int The degree to which members of the series
    :return: int|real
    """
    the_sum = 0
    for i in num_list:
        the_sum += math.fabs(i) ** mod
    return the_sum


def norm_infinite(matrix):
    """
    The infinite matrix norm
    :param matrix: list
    :return:
    """
    norm = []
    for i in range(len(matrix)):
        norm.insert(i, list_sum(matrix[i]))
    return max(norm)


def norm_first(matrix):
    """
    The first norm of the matrix
    :param matrix: list
    :return:
    """
    matrix_t = list(zip(*matrix))
    return norm_infinite(matrix_t)


def norm_second(matrix):
    """
    The second norm of the matrix
    :param matrix:
    :return:
    """
    norm = []
    for i in range(len(matrix)):
        norm.append(list_sum(matrix[i], 2))
    return round(math.sqrt(list_sum(norm)), 4)


def get_matrix_diagonal_values(matrix):
    """
    Get matrix diagonal values
    :param matrix: list
    :return: list
    """
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
    """
    Set matrix diagonal values
    :param matrix: list
    :param value:
    :return:
    """
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


def matrix_addition(first_matrix, second_matrix, addition=1):
    """
    Addition of matrices is performed only when the matrices have the same dimension
    :param first_matrix: list
    :param second_matrix: list
    :param addition: int Addition flag. If 1, then addition, if -1 subtraction
    :return: list
    """
    try:
        if len(first_matrix) == 0 or len(second_matrix) == 0:
            raise ValueError(1)
        if len(first_matrix) != len(second_matrix) or len(first_matrix[0]) != len(second_matrix[0]):
            raise ValueError(2)
        if math.fabs(addition) != 1:
            raise ValueError(3)
    except ValueError as e:
        if 1 in e.args:
            print("The matrices can not be empty")
        elif 2 in e.args:
            print("The matrices must be of the same dimension")
        elif 3 in e.args:
            print("Invalid addition coefficient")
    else:
        new_matrix = [0] * len(first_matrix)
        for i in range(len(first_matrix)):
            new_matrix[i] = [0] * len(first_matrix[0])
            for j in range(len(second_matrix[0])):
                new_matrix[i][j] = first_matrix[i][j] + addition * second_matrix[i][j]
        return new_matrix


def matrix_multiplication(first_matrix, second_matrix, accuracy=4):
    """
    Matrix multiplication
    :param first_matrix: list
    :param second_matrix: list
    :param accuracy: int Rounding accuracy of values in decimal places
    :return:
    """
    try:
        if len(first_matrix[0]) != len(second_matrix):
            raise ValueError(1)
        if type(accuracy) != int:
            raise TypeError
        if accuracy <= 0:
            raise ValueError(2)
    except ValueError as e:
        if 1 in e.args:
            print("The dimension of the matrices is not suitable for multiplication")
        elif 2 in e.args:
            print("The accuracy of calculation can not be negative or null")
    except TypeError:
        print("The accuracy type must be int")
    else:
        new_matrix = [0] * len(first_matrix)
        for i in range(len(first_matrix)):
            new_matrix[i] = [0] * len(second_matrix[0])
            for j in range(len(second_matrix[0])):
                value = 0
                for k in range(len(second_matrix)):
                    value += first_matrix[i][k] * second_matrix[k][j]
                new_matrix[i][j] = round(value, accuracy)
        return new_matrix


def matrix_multiplication_by_number(first_matrix, value, division=0, accuracy=4):
    """
    Matrix multiplication by number
    :param first_matrix: list
    :param value: list|int
    :param division: int Division flag. If 0, than multiplication, else division
    :param accuracy: int Rounding accuracy of values in decimal places
    :return:
    """
    try:
        if accuracy <= 0:
            raise ValueError(1)
        if type(value) != list and type(value) != int:
            raise TypeError(1)
        if type(accuracy) != int:
            raise TypeError(2)
    except ValueError as e:
        if 1 in e.args:
            print("The accuracy of calculation can not be negative or null")
    except TypeError as e:
        if 1 in e.args:
            print("Value must be list or int type")
        if 2 in e.args:
            print("Accuracy must be list or int type")
    else:
        new_matrix = [0] * len(first_matrix)

        if type(value) == list:
            if (len(first_matrix)) == 1:
                first_matrix = list(zip(*first_matrix))
            for i in range(len(first_matrix)):
                new_matrix[i] = [0] * len(first_matrix[i])
                for j in range(len(first_matrix[i])):
                    if division == 0:
                        new_matrix[i][j] = round(first_matrix[i][j] * value[i][0], accuracy)
                    else:
                        new_matrix[i][j] = round(first_matrix[i][j] / value[i][0], accuracy)

        elif type(value) == int:
            for i in range(len(first_matrix)):
                new_matrix[i] = [0] * len(first_matrix[i])
                for j in range(len(first_matrix[i])):
                    if division == 0:
                        new_matrix[i][j] = round(first_matrix[i][j] * value, accuracy)
                    else:
                        new_matrix[i][j] = round(first_matrix[i][j] / value, accuracy)

        return new_matrix


def iterations_number(norm_b, norm_c, r=0.01):
    """
    Iterations number
    :param norm_b:
    :param norm_c:
    :param r: Accuracy of values
    :return:
    """
    try:
        if my_error.SubZeroError.check(norm_b, norm_c):
            raise my_error.SubZeroError(norm_b, norm_c)
    except my_error.SubZeroError as e:
        print(e.msg)
    else:
        number = math.log((r * (1 - norm_c)) / norm_b) / math.log(norm_c)
        return round(number)


def iteration(b_matrix, c_matrix, x_matrix, iteration_number, r=ACCURACY, i=0):
    """
    Iteration method
    :param b_matrix:
    :param c_matrix:
    :param x_matrix:
    :param iteration_number: int Iterations number
    :param r: Accuracy of values
    :param i: int Current iteration number
    :return: list
    """
    try:
        if len(b_matrix) == 0 or len(c_matrix) == 0 or len(x_matrix) == 0:
            raise ValueError(1)
        if iteration_number <= 0:
            raise ValueError(2)
    except ValueError as e:
        if 1 in e.args:
            print("The matrices can not be empty")
        if 2 in e.args:
            print("The number of iterations can not be negative or null")
    else:
        new_matrix = matrix_addition(b_matrix, matrix_multiplication(c_matrix, x_matrix), -1)
        delta = norm_infinite(matrix_addition(new_matrix, x_matrix, -1))
        if i in range(iteration_number) and delta > r:
            i += 1
            new_matrix = iteration(b_matrix, c_matrix, new_matrix, iteration_number, r, i)
        return new_matrix


a_array = [
    [0.95 + C, 0.26 + C, (-0.17) + C, 0.27 + C],
    [(-0.15) + C, 1.26 + C, 0.36 + C, 0.42 + C],
    [0.26 + C, (-0.54) + C, (-1.76) + C, 0.31 + C],
    [(-0.44) + C, 0.29 + C, (-0.78) + C, (-1.78) + C]
]

z_array = [
    [2.48], [(-3.16)], [1.52], [(-1.29)]
]

for i in range(len(a_array)):
    for j in range(len(a_array[i])):
        a_array[i][j] = round(a_array[i][j], 4)

c_array = matrix_multiplication_by_number(a_array, get_matrix_diagonal_values(a_array), 1)
c_array = set_matrix_diagonal_values(c_array)
c_norm = norm_infinite(c_array)
b_array = matrix_multiplication_by_number(z_array, get_matrix_diagonal_values(a_array), 1)
b_norm = norm_infinite(b_array)
n = iterations_number(b_norm, c_norm, ACCURACY)

print(iteration(b_array, c_array, b_array, n, ACCURACY))
