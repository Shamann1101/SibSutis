def backpack_fill(backpack, price, n):
    if n < 0:
        return backpack
    if n not in backpack:
        backpack[n] = 0
    for item in price:
        item = n - item
        if item not in backpack and item >= 0:
            backpack[item] = 0
            backpack_fill(backpack, price, item)
    return backpack


def backpack_set_weights(backpack, price, n):
    if n < 0:
        return -1
    elif n == 0:
        return 0
    if n in price:
        backpack[n] = price[n]
        return price[n]
    if backpack[n] > 0:
        return backpack[n]
    weights = []
    for item in price:
        weight = backpack_set_weights(backpack, price, n - item)
        if weight >= 0:
            weight += price[item]
        weights.append(weight)
    max_weight = max(weights)
    if max_weight < 0:
        max_weight = 0
    backpack[n] = max_weight
    return max_weight


def backpack_clean(backpack):
    backpack_new = {}
    for key in backpack:
        if backpack[key] > 0:
            backpack_new[key] = backpack[key]
    return backpack_new


def main():
    price = {
        3: 8,
        5: 14,
        8: 23
    }
    backpack = {}

    n = 13

    print(backpack_fill(backpack, price, n))

    print(backpack_set_weights(backpack, price, n))

    print(backpack)

    print(backpack_clean(backpack))


if __name__ == '__main__':
    main()
