from random import randint


def parentheses(widths: list) -> tuple:
    print("widths:", widths)
    res, history = dict(), dict()
    n = len(widths) - 1
    for i in range(n):
        res[i, i] = 0
        history[i, i] = (i, i)
    for i in range(1, n, 1):
        for k in range(n - i):
            j = k
            values = {}
            while j < k + i:
                value = res[k, j] + res[j + 1, k + i] + widths[k] * widths[j + 1] * widths[k + i + 1]
                values[value] = ((k, j), (j + 1, k + i))
                print(
                    f'f({k}, {k + i}) = f({k},{j}) + f({j + 1},{k + i}) + {widths[k]} * {widths[j + 1]} * {widths[k + i + 1]} = {value}')
                j += 1
            res[k, k + i] = min(values.keys()) if len(values.keys()) > 0 else 0
            history[k, k + i] = values.get(res[k, k + i])
    return res, history


def restore(history: dict, widths: list, index: tuple):
    if type(history[index][0]) == tuple:
        f1 = restore(history, widths, history[index][0])
        f2 = restore(history, widths, history[index][1])
        return f'({f1}{f2})'
    else:
        return f'A{history[index][0]}'


def main():
    # widths = [10, 20, 50, 1, 100]
    # widths = [5 for _ in range(11)]
    widths = [randint(1, 100) for _ in range(11)]
    # print(widths)
    res, history = parentheses(widths)
    rest = restore(history, widths, (0, len(widths) - 2))
    # print(res)
    print('restore', rest)


if __name__ == '__main__':
    main()
