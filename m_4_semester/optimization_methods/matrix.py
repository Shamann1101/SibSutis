def calculate(_matrix: list) -> int:
    if len(_matrix) == 0:
        raise ValueError('Matrix is empty')

    matrix = _matrix.copy()
    matrix.insert(len(matrix), [0 for _ in range(len(matrix[0]) + 1)])
    for i in range(len(matrix) - 1):
        matrix[i].insert(0, 0)
    # print(matrix)  # FIXME
    rm = []
    for _ in range(len(matrix)):
        rm.append([0 for _ in range(len(matrix[0]))])
    for i in range(len(matrix) - 2, -1, -1):
        for j in range(1, len(matrix[0]), 1):
            # print(f'matrix[{i}][{j}] = {matrix[i][j]}')  # FIXME
            rm[i][j] = max(rm[i + 1][j], rm[i][j - 1], rm[i + 1][j - 1]) + matrix[i][j]
    # print(rm, 'result')  # FIXME
    return rm[0][-1]


def _main():
    matrix = [
        [2, 1, 2, 3, 3],
        [8, 7, 5, 5, 4],
        [8, 3, 2, 4, 1],
        [3, 1, 2, 3, 1],
        [5, 9, 2, 1, 2],
    ]
    print(calculate(matrix))


if __name__ == '__main__':
    _main()
