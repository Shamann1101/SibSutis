from math import inf


def _fill(_d: dict, _l: list, n: int):
    for l in _l:
        if not _d.get(l):
            _d[l] = dict()
        for i in range(n):
            if _d[l].get(i) is None:
                _d[l][i] = inf


def _jump(_d: dict, _pos: list) -> int:
    for pos in _pos[1:]:
        for l in _d[pos].keys():
            d = min(_d.get(pos - l, {}).get(l, inf),
                    _d.get(pos - l, {}).get(l - 1, inf),
                    _d.get(pos - l, {}).get(l + 1, inf))
            _d[pos][l] = min(d + 1, _d[pos][l])

    return min(_d[_pos[-1]].values())


def _restore(_d: dict) -> list:
    keys = _d.keys()
    keys = sorted(keys)
    keys.reverse()
    current_position = max(_d.keys())
    current_l = min(_d[current_position].values())
    result = [(current_position, current_l)]
    while True:
        parent_pos, parent_l = _get_previous(_d, current_position, current_l)
        if parent_pos <= 0:
            break
        result.append((parent_pos, parent_l))
        current_position, current_l = parent_pos, parent_l
    return result


def _get_previous(_d: dict, pos: int, l: int) -> tuple:
    if l == inf:
        return 0, 0
    k = _get_key_by_value(_d, pos, l)
    kk = _get_key_by_value(_d, pos - k, l - 1)
    return pos - k, _d[pos - k][kk]


def _get_key_by_value(_d: dict, pos: int, _v: int) -> int:
    return list(_d[pos].keys())[list(_d[pos].values()).index(_v)]


def _main():
    l = [0, 1, 2, 3, 5, 7, 10, 12, 14, 17]
    d = {0: {0: 0}}  # pos: {l: price}
    _fill(d, l, 5)
    print(_jump(d, l))
    print(d)
    print(_restore(d))


if __name__ == '__main__':
    _main()
