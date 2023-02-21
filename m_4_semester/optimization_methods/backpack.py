from __future__ import annotations

import copy
import math
import operator


class Item:
    def __init__(self, price: int, weight: int, title: str = None):
        if price <= 0 or weight <= 0:
            raise ValueError('Price and weight must be positive int')
        self._price = price
        self._weight = weight
        self.title = title

    @property
    def price(self) -> int:
        return self._price

    @property
    def weight(self) -> int:
        return self._weight

    def __str__(self):
        return self.title or str(self._weight)

    def __repr__(self):
        return "Item {} price: {}".format(self.title or self._weight, self._price)

    def __eq__(self, other):
        return (self._price, self._weight, self.title) == (other.price, other.weight, other.title)

    def __hash__(self):
        return hash((self._price, self._weight, self.title))


class Backpack:
    _history = {}

    def __init__(self, weight_limit: int, stock: Stock, *args):
        if weight_limit < 0:
            raise ValueError('Weight limit must be positive int')
        self._weight_limit = weight_limit
        self._stock = stock

        bp = self.get_from_history_by_weight(weight_limit)
        if bp:
            self._kit = bp.kit.copy()
            self._parent = bp.parent
            self._stock = copy.deepcopy(bp.stock)
        else:
            self._kit = {}  # {Item: int}
            self._parent = None
            if args and type(args[0]) == Backpack:
                self.parent = args[0]

    # def __del__(self):
    #     for item, count in self._kit.items():
    #         self._stock.add_item(item, count)
    #         print(f'Put item back {item}')

    def __str__(self):
        return str(self._weight_limit) + str(self._kit)

    def __repr__(self):
        return "price: " + str(self.price) + "\tkit: " + str(self._kit) + "\tstock: " + str(self._stock) + "\n"

    @classmethod
    @property
    def history(cls) -> dict:
        return cls._history

    @property
    def parent(self) -> Backpack | None:
        return self._parent

    @parent.setter
    def parent(self, parent: Backpack):
        if self._weight_limit <= parent.weight_limit:
            raise ValueError('Parent\'s weight limit must be smaller than child\'s')
        self._parent = parent
        self._kit = self._parent.kit.copy()

    @property
    def weight_limit(self) -> int:
        return self._weight_limit

    @property
    def kit(self) -> dict:
        return self._kit

    @property
    def price(self) -> int:
        return sum([i.price * c for i, c in self._kit.items()])

    @property
    def free_space(self) -> int:
        return self._weight_limit - sum([i.weight * c for i, c in self._kit.items()])

    @property
    def parent_list(self) -> list:
        if self._parent is None:
            return []
        pl = [self._parent]
        pl.extend(self._parent.parent_list)
        return pl

    @property
    def stock(self) -> Stock:
        return self._stock

    def _init_kit(self, kit: dict):
        for item, count in kit.items():
            if type(item) != Item:
                raise TypeError('Value is not Item class')
        self._kit = kit

    @classmethod
    def get_from_history_by_weight(cls, weight: int) -> Backpack | None:
        return cls._history.get(weight)

    def add_item(self, item: Item):
        if item.weight > self.free_space:
            raise ValueError(
                'Not enough weight for this item. Free: {}, weight: {}'.format(self.free_space, item.weight))
        if item not in self._kit:
            self._kit[item] = 1
        else:
            self._kit[item] += 1

    @classmethod
    def fill_history(cls, weight_limit: int, _stock: Stock):
        bacpack_list = []

        stock = copy.deepcopy(_stock)
        for i in range(weight_limit + 1):
            for item in stock.stock.copy():
                if i < item.weight:
                    continue

                try:
                    bp_wo_item = Backpack(i - item.weight, copy.deepcopy(stock))
                except ValueError:
                    continue

                bpp = Backpack(i, bp_wo_item.stock)
                bpp.parent = bp_wo_item
                if bpp.stock.can_get_item(item):
                    bpp.add_item(bpp.stock.pop_item(item))
                    bacpack_list.append(bpp)

            if len(bacpack_list) > 0:
                bp = max(bacpack_list, key=operator.attrgetter('price'))
            else:
                bp = Backpack(i, stock)

            cls._history[i] = bp
            stock = copy.deepcopy(bp.stock)

    def fill(self):
        self.fill_history(self._weight_limit, self._stock)


class Stock:
    def __init__(self, *args):
        self._stock = dict()  # {Item: int)
        if args and type(args[0]) == dict:
            self._init_stock(args[0])

    def __repr__(self):
        return str(self._stock)

    @property
    def stock(self) -> dict:
        return self._stock

    def _init_stock(self, stock: dict):
        for item, count in stock.items():
            if type(item) != Item:
                raise TypeError('Value is not Item class')
        self._stock = stock

    def add_item(self, item: Item, count: int = None):
        if item not in self._stock:
            self._stock[item] = count or math.inf

    def pop_item(self, item: Item) -> Item:
        if item not in self._stock:
            raise ValueError

        self._stock[item] -= 1

        if self._stock[item] == 0:
            del self._stock[item]

        return item

    def can_get_item(self, item: Item) -> bool:
        return True if self._stock.get(item) else False


def _main():
    first = Item(price=8, weight=3)
    second = Item(price=14, weight=5)
    third = Item(price=23, weight=8)

    stock = Stock()
    stock.add_item(first, 3)
    stock.add_item(second, 2)
    stock.add_item(third, 1)
    print('stock', stock)

    weight_limit = 13
    Backpack.fill_history(weight_limit, stock)
    backpack = Backpack(weight_limit, stock)
    # backpack.fill()
    print('backpack', backpack, backpack.price)
    print('history', Backpack.history)
    print('parent_list', backpack.parent_list)


if __name__ == '__main__':
    _main()
