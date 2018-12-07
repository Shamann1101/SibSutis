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
        print(f'Find max: {column}, {maximum}, {maximum_index}')

        temp = gauss_data[index]
        gauss_data[index] = gauss_data[index + maximum_index]
        gauss_data[index + maximum_index] = temp
        del temp

        print_array(gauss_data)
        is_fill, is_calculate = False, False
        calculate_count = 0
        while not is_fill or not is_calculate:
            # print("New iteration")
            for string in range(index, len(gauss_data)):
                for elem in range(index, len(gauss_data[string])):
                    # print(f'index: {index}, string: {string}, elem: {elem}, is_calculate: {is_calculate}')
                    if string == index:
                        if is_calculate or index == len(gauss_data) - 1:
                            print(f'source: {gauss_data[string][elem]}, maximum: {maximum}')
                            gauss_data[string][elem] /= maximum
                            if index == len(gauss_data) - 1:
                                is_fill, is_calculate = True, True
                    elif elem == index:
                        if is_calculate:
                            gauss_data[string][elem] = 0
                            is_fill = True
                    elif not is_calculate:
                        # print(string, elem)
                        gauss_data[string][elem] = gauss_data[string][elem] - (gauss_data[index][elem] * gauss_data[string][index]) / maximum
                        calculate_count += 1
                        if calculate_count == (len(gauss_data) - index - 1) * (len(gauss_data[string]) - index - 1):
                            is_calculate = True

                # print(gauss_data[string])
        print_array(gauss_data)
        # if index == 3:
        #     break
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
