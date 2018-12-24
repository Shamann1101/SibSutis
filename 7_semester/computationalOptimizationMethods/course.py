from math import fabs

ACCURACY = 1e-5


excluded_columns = []


def find_minimal_m(arr, excluded_arr):
    minimum = max(arr)
    minimum_index = arr.index(minimum)
    for i in range(len(arr)):
        if i in excluded_arr:
            continue
        if arr[i] < minimum and arr[i] != 0:
            minimum = arr[i]
            minimum_index = i
    return minimum, minimum_index


def find_minimal_co(arr):
    minimum = max(arr)
    minimum_index = arr.index(minimum)
    for i in range(len(arr)):
        if arr[i] < 0:
            continue
        elif arr[i] < minimum:
            minimum = arr[i]
            minimum_index = i
    return minimum, minimum_index


def is_positive_list(arr):
    if min(arr) < 0:
        return False
    else:
        return True


def print_array(arr):
    print()
    for i in arr:
        print(i)
    print()


def transfiguration(source_data, index_row, index_col):
    global excluded_columns
    data = source_data.copy()
    i_row = index_row.copy()
    i_col = index_col.copy()
    print("Source data:")
    print_array(data)

    while not is_positive_list(data[-1][:-1]) or not is_positive_list(data[-2][:-1]):
        ind = -1 if not is_positive_list(data[-1][:-1]) else -2
        m_row = [i for i in data[ind]]
        minimum_m, maximum_m_index = find_minimal_m(m_row[:-1], excluded_columns)
        print("m_row:", m_row, minimum_m, maximum_m_index)

        for row in range(len(i_col)):
            if len(data[row]) == len(i_row) + 1:
                simplex = data[row][-1] / data[row][maximum_m_index]
                data[row].append(simplex)
            elif len(data[row]) == len(i_row) + 2:
                if data[row][maximum_m_index] == 0:
                    Exception("zero:", row, maximum_m_index)
                    # print("zero:", row, maximum_m_index)
                simplex = data[row][-2] / data[row][maximum_m_index]
                data[row][-1] = simplex
            else:
                print("Something gone wrong")
                return

        m_col = [data[i][-1] for i in range(len(i_col))]
        minimum_co, minimum_co_index = find_minimal_co(m_col)
        print("m_col:", m_col, minimum_co, minimum_co_index)

        for row in range(len(data)):
            if row == minimum_co_index:
                continue
            for elem in range(len(i_row) + 1):
                if elem == maximum_m_index or elem in excluded_columns:
                    continue
                data[row][elem] -= data[row][maximum_m_index] * data[minimum_co_index][elem] / data[minimum_co_index][maximum_m_index]
                if fabs(data[row][elem]) < ACCURACY:
                    data[row][elem] = 0

        base_value = data[minimum_co_index][maximum_m_index]
        for row in range(len(data)):
            for elem in range(len(i_row) + 1):
                if elem in excluded_columns:
                    continue
                elif row == minimum_co_index:
                    data[row][elem] /= base_value
                    if fabs(data[row][elem]) < ACCURACY:
                        data[row][elem] = 0
                elif elem == maximum_m_index:
                    data[row][elem] = 0

        print(f'Swap {i_row[maximum_m_index]} to {i_col[minimum_co_index]}')
        i_row[maximum_m_index], i_col[minimum_co_index] = i_col[minimum_co_index], i_row[maximum_m_index]
        excluded_columns.append(maximum_m_index)

        print_array(data)
        print(i_row, i_col)
    print("\n")
    return data, i_row, i_col


def main():
    source_data = [
        [5, 1, -1, 0, 0, 12],
        [5, 4, 0, -1, 0, 33],
        [2, 5, 0, 0, -1, 20],
        [11, 1, 0, 0, 0, 0],
        [-12, -10, 1, 1, 1, -65]
    ]

    doris_data = [
        [5, 3, -1, 0, 0, 30],
        [2, 4, 0, -1, 0, 26],
        [3, 11, 0, 0, -1, 54],
        [5, 2, 0, 0, 0, 0],
        [-10, -18, 1, 1, 1, -110]
    ]

    index_row = [i for i in range(5)]
    index_col = [i for i in range(5, 8)]

    transfiguration(source_data, index_row, index_col)


if __name__ == '__main__':
    main()
