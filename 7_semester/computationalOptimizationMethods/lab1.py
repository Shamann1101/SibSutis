from math import fabs


def print_array(arr):
    print()
    for i in arr:
        print(i)
    print()


def gauss(data):
    gauss_data = data.copy()
    for index in range(len(gauss_data)):
        print(f'Index: {index}')
        column = []
        for string in range(index, len(gauss_data)):
            column.append(fabs(gauss_data[string][index]))
        maximum = max(column)  # Get unsigned value
        maximum_index = column.index(maximum)
        maximum = gauss_data[index + maximum_index][index]  # Get signed value
        # print(f'Find max: {column}, {maximum}, {maximum_index}')

        temp = gauss_data[index]
        gauss_data[index] = gauss_data[index + maximum_index]
        gauss_data[index + maximum_index] = temp
        del temp

        # print_array(gauss_data)
        is_fill, is_calculate = False, False
        while not is_fill or not is_calculate:
            for string in range(len(gauss_data)):
                for elem in range(index+1, len(gauss_data[string])):
                    if string == index:
                        continue
                    gauss_data[string][elem] = gauss_data[string][elem] - (gauss_data[index][elem] * gauss_data[string][index]) / maximum
            is_calculate = True

            for string in range(len(gauss_data)):
                for elem in range(len(gauss_data[string])):
                    if string == index and elem >= index:
                        gauss_data[string][elem] /= maximum
                    elif elem == index:
                        gauss_data[string][elem] = 0
            is_fill = True

        print_array(gauss_data)
    return gauss_data


def main():
    source_data = [
        [15, -5, 8, 11, -6, -76],
        [15, 1, 7, 1, 11, -79],
        [-5, 11, 5, -9, 10, -6],
        [13, -5, -1, 11, 3, -27],
        [15, 4, -3, -1, 3, -4]
    ]

    method_data = [
        [1, -7, 4, -3, -3, -12],
        [-1, -5, 7, -1, 4, 30],
        [-6, 7, 7, 5, 7, 49],
        [-5, -3, -6, -3, 8, -7],
        [-5, -5, -2, -3, -6, -67]
    ]

    gauss(method_data)


if __name__ == '__main__':
    main()
