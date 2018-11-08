from random import randint


def array_fill(n):
    """
    Return array full of random numbers
    :param n: limit
    :return: array
    """
    try:
        if n <= 0:
            raise ValueError
    except ValueError:
        print("Limit must be positive number")
    else:
        arr = [0] * n
        for i in range(n):
            while True:
                rand_int = randint(0, n)
                if rand_int not in arr:
                    arr[i] = rand_int
                    break
        return arr


def array_merge(first_array, second_array):
    """
    Returns merged up sorted array
    :param first_array:
    :param second_array:
    :return:iteration
    """
    try:
        if len(first_array) < 1 or len(second_array) < 1:
            raise ValueError
    except ValueError:
        print("Array's length must be positive")
    else:
        result_array = [0] * (len(first_array) + len(second_array))
        i, j = 0, 0

        for n in range(len(result_array)):
            if i == len(first_array):
                result_array[n:] = second_array[j:]
                break
            elif j == len(second_array):
                result_array[n:] = first_array[i:]
                break

            if first_array[i] < second_array[j]:
                result_array[n] = first_array[i]
                i += 1
            else:
                result_array[n] = second_array[j]
                j += 1

        return result_array


def merge_sort(source_array):
    numbers = 1
    result_array = source_array
    while numbers < len(result_array):
        pair = 0
        while (pair+1)*numbers*2 <= len(result_array):
            print(result_array[pair*numbers*2:(pair+1)*numbers*2])
            pair += 1
        break


if __name__ == '__main__':
    n = 11
    arr = array_fill(n)
    print(arr)
    merge_sort(arr)
    # print(array_merge(arr[:int(n/2)], arr[int(n/2):]))
