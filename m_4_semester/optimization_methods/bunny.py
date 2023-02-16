CONST_SWAMP = 'w'
CONST_FEED = '"'


def bunny(_in: list) -> int:
    if len(_in) == 0:
        raise ValueError('List is empty')
    elif len(_in) == 1:
        return 0

    _list = [-1 for _ in range(len(_in))]
    _list[0] = 0

    for i in range(1, len(_list), 1):
        if _in[i] == CONST_SWAMP:
            continue

        if i < 2:
            _list[i] = _list[i - 1]
        elif i < 4:
            _list[i] = max(_list[i - 1], _list[i - 3])
        else:
            _list[i] = max(_list[i - 1], _list[i - 3], _list[i - 5])

        if _in[i] == CONST_FEED:
            _list[i] += 1

    return _list[-1]


def main():
    _in = ['.', '.', '.', CONST_SWAMP, CONST_FEED, CONST_FEED, CONST_SWAMP, '.']
    print(bunny(_in))


if __name__ == '__main__':
    main()