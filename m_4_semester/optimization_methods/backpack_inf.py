from copy import deepcopy


def fill_history(history: dict, price: dict, n: int):
    if n < 0:
        raise ValueError
    for i in range(n + 1):
        history[i] = dict.fromkeys(price.keys(), 0)


def pack(history_dict: dict, price_dict: dict) -> int:
    history_keys = list(history_dict.keys())
    history_keys.sort()
    for i in history_keys:
        bp_list = []
        for item in price_dict.keys():
            if i < item:
                continue

            bp = deepcopy(history_dict.get(i - item))
            if bp is None:
                continue

            bp[item] += 1
            bp_list.append(bp)

        if len(bp_list) > 0:
            m = max(bp_list, key=lambda x: sum([price_dict[item] * count for item, count in x.items()]))
            history_dict[i] = m

    return sum([price_dict[item] * count for item, count in history_dict[history_keys[-1]].items()])


def main():
    price = {
        3: 8,
        5: 14,
        8: 23
    }
    history = {}
    n = 1_000_000
    # n = 13
    fill_history(history, price, n)
    p = pack(history, price)
    print(p, history[n])


if __name__ == '__main__':
    main()
