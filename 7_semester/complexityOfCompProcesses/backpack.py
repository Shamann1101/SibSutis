class Backpack:
    def __init__(self, title, *args):
        self.title = title
        self.price = 0
        self.parent = None
        self.kit = {}
        if args:
            if type(args[0]) == dict:
                for item in args[0]:
                    self.kit[item] = 0

    def __str__(self):
        return str(self.title) + str(self.kit)

    def __repr__(self):
        return "price: " + str(self.price) + "\tkit: " + str(self.kit) + "\n"


def backpack_fill(backpack, price, n):
    if n < 0:
        return backpack
    if n not in backpack:
        backpack[n] = Backpack(n, price)
    for item in price:
        item = n - item
        if item not in backpack and item >= 0:
            backpack[item] = Backpack(item, price)
            backpack_fill(backpack, price, item)
    return backpack


def backpack_set_prices(backpack, price, n):
    if n < 0:
        return -1
    elif n == 0:
        return 0
    if n in price:
        backpack[n].price = price[n]
        backpack[n].kit[n] = 1
        return price[n]
    if backpack[n].price > 0:
        return backpack[n].price
    weights = price.copy()
    for item in price:
        weight = backpack_set_prices(backpack, price, n - item)
        if weight >= 0:
            weight += price[item]
        weights[item] = weight
    max_weight_price = max(weights, key=weights.get)
    max_weight = 0
    if weights[max_weight_price] > 0:
        max_weight = weights[max_weight_price]
        backpack[n].kit = backpack[n - max_weight_price].kit.copy()
        backpack[n].kit[max_weight_price] += 1
    backpack[n].price = max_weight
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

    print(backpack_set_prices(backpack, price, n))

    print(backpack)
    #
    # print(backpack_clean(backpack))


if __name__ == '__main__':
    main()
