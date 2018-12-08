from math import fabs


def is_positive_list(arr):
    for i in arr:
        if i < 0:
            return False
    return True


def print_array(arr):
    print()
    for i in arr:
        print(i)
    print()


def transfiguration(source_data, index_row, index_col):
    data = source_data.copy()
    i_row = index_row.copy()
    i_col = index_col.copy()

    m_row = [fabs(i) for i in data[-1]]
    maximum_m = max(m_row[:-1])
    maximum_m_index = m_row.index(maximum_m)
    # print(m_row, maximum_m, maximum_m_index)

    for row in range(len(i_col)):
        # print(f'{source_data[row][-1]} / {source_data[row][maximum_m_index]}')
        if len(data[row]) == len(i_row) + 1:
            simplex = data[row][-1] / data[row][maximum_m_index]
            data[row].append(simplex)
        elif len(data[row]) == len(i_row) + 2:
            simplex = data[row][-2] / data[row][maximum_m_index]
            data[row][-1] = simplex
        else:
            print("Something gone wrong")
            return

    m_col = [data[i][-1] for i in range(len(i_col))]
    minimum_co = min(m_col)
    minimum_co_index = m_col.index(minimum_co)
    # print(m_col, minimum_co, minimum_co_index)

    for row in range(len(data)):
        if row == minimum_co_index:
            continue
        for elem in range(len(i_row) + 1):
            if elem == maximum_m_index:
                continue
            data[row][elem] -= data[row][maximum_m_index] * data[minimum_co_index][elem] / data[minimum_co_index][maximum_m_index]
            # print(data[row][elem])

    base_value = data[minimum_co_index][maximum_m_index]
    for row in range(len(data)):
        for elem in range(len(i_row) + 1):
            if row == minimum_co_index:
                data[row][elem] /= base_value
            elif elem == maximum_m_index:
                data[row][elem] = 0

    tmp = i_row[maximum_m_index]
    i_row[maximum_m_index] = i_col[minimum_co_index]
    i_col[minimum_co_index] = tmp
    del tmp

    print_array(data)
    print(i_row, i_col)
    return data, i_row, i_col


def main():
    source_data = [
        [5, 1, -1, 0, 0, 12],
        [5, 4, 0, -1, 0, 33],
        [2, 5, 0, 0, -1, 20],
        [11, 1, 0, 0, 0, 0],
        [-12, -10, 1, 1, 1, -65]
    ]

    index_row = [i for i in range(5)]
    index_col = [i for i in range(5, 8)]

    # m_row = [fabs(i) for i in source_data[-1]]
    # maximum_m = max(m_row[:-1])
    # maximum_m_index = m_row.index(maximum_m)
    #
    # for row in range(len(index_col)):
    #     # print(f'{source_data[row][-1]} / {source_data[row][maximum_m_index]}')
    #     source_data[row].append(source_data[row][-1] / source_data[row][maximum_m_index])
    #
    transfiguration(source_data, index_row, index_col)


if __name__ == '__main__':
    main()
