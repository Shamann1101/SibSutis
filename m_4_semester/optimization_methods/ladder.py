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


def _get_list(filename: str = 'ladder.in') -> list:
    with open(filename, 'r') as f:
        count = int(f.readline())
        value_list = f.readline().split(' ', count)
        return [int(v.strip()) for v in value_list]


def _save_result(value: int, filename: str = 'ladder.out'):
    with open(filename, 'w') as f:
        f.write(str(value))


def main():
    _list = _get_list()
    result = ladder(_list)
    _save_result(result)


if __name__ == '__main__':
    main()
