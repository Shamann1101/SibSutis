from random import sample
import argparse


def array_merge(first_array, second_array):
    """
    Returns merged up sorted array
    :param first_array:
    :param second_array:
    :return:iteration
    """
    try:
        if len(first_array) < 1 and len(second_array) < 1:
            raise ValueError
    except ValueError:
        print("Array's length must be positive")
    else:
        if len(first_array) < 1:
            return second_array
        elif len(second_array) < 1:
            return first_array

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
    """
    Returns merge-sorted array. Sort using without recursion
    :param source_array:
    :return:
    """
    try:
        if len(source_array) < 1:
            raise ValueError
    except ValueError:
        print("Array's length must be positive")
    else:
        numbers = 1
        result_array = source_array.copy()
        while numbers < len(result_array):
            pair, left_limit = 0, 0
            while left_limit <= len(result_array):
                if 0 < len(result_array[left_limit:]) <= numbers:
                    if args.print:
                        print(result_array[left_limit:])
                    result_array[left_limit:] = array_merge(result_array[left_limit:], [])
                elif len(result_array[left_limit:]) > 0:
                    if args.print:
                        print(result_array[left_limit:left_limit+numbers],
                              result_array[left_limit+numbers:(pair+1)*numbers*2])
                    result_array[left_limit:(pair+1)*numbers*2] = \
                        array_merge(result_array[left_limit:left_limit+numbers],
                                    result_array[left_limit+numbers:(pair+1)*numbers*2])
                pair += 1
                left_limit = pair * numbers * 2
            numbers *= 2
        return result_array


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Merge sorting')
    parser.add_argument('limit', type=int, nargs='?', help='Size of sample array. Default 11')
    parser.add_argument('--print', action='store_true', help='Print log')
    args = parser.parse_args()

    limit = int(args.limit) if args.limit and args.limit > 0 else 11
    new_array = sample(range(limit), limit)
    print("Source array:", new_array)
    sorted_array = merge_sort(new_array)
    print("Sorted array:", sorted_array)
