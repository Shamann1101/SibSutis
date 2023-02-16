def ladder(_in: list) -> int:
    if len(_in) == 0:
        raise ValueError('Ladder is empty')
    elif len(_in) == 1:
        return _in[0]

    _list = [0]
    _list.extend(_in)
    for i in range(len(_list) - 2):
        _list[i + 2] = max([_list[i], _list[i + 1]]) + _list[i + 2]

    return _list[-1]


def main():
    _list = [3, 1, -4, 1, 5, 9, -2, -6]
    print(ladder(_list))


if __name__ == '__main__':
    main()
