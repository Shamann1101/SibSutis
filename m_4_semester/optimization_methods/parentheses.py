def parentheses(widths: list) -> dict:
    print("widths:", widths)
    res = dict()
    n = len(widths) - 1
    for i in range(n):
        res[i, i] = 0
    for i in range(1, n, 1):
        for k in range(n - i):
            j = k
            values = []
            while j < k + i:
                value = res[k, j] + res[j + 1, k + i] + widths[k] * widths[j + 1] * widths[k + i + 1]
                values.append(value)
                print(
                    f'f({k}, {k + i}) = f({k},{j}) + f({j + 1},{k + i}) + {widths[k]} * {widths[j + 1]} * {widths[k + i + 1]} = {value}')
                j += 1
            res[k, k + i] = min(values) if len(values) > 0 else 0
    return res


def main():
    widths = [10, 20, 50, 1, 100]
    print(parentheses(widths))


if __name__ == '__main__':
    main()
