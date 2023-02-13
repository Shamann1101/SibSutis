from itertools import permutations
from random import shuffle
from time import time

import numpy as np

N_ITER = 10


def main():
    # loading data
    f = open("datasets/salesman010.txt", 'r').read().splitlines()
    num_cities = f.pop(0)
    cities = np.array([tuple(map(float, coord.split())) for coord in f])
    print('Cities loaded')

    for algorithm in [_brute_force, _branch_bound]:
        # calculating path
        start = time()
        print('Calculating path')
        path, length = algorithm(cities)
        print(path)

        to_time = time() - start
        print("Found path of length %s in %s seconds" % (round(length, 2), round(to_time, 2)))


def _dist_squared(c1, c2):
    t1 = c2[0] - c1[0]
    t2 = c2[1] - c1[1]

    return t1 ** 2 + t2 ** 2


def _calc_length(cities, path):
    length = 0
    for i in range(len(path)):
        length += _dist_squared(cities[path[i - 1]], cities[path[i]])

    return length


def _brute_force(cities):
    min_length = _calc_length(cities, range(len(cities)))
    min_path = range(len(cities))

    for path in permutations(range(len(cities))):
        length = _calc_length(cities, path)
        if length < min_length:
            min_length = length
            min_path = path

    return min_path, min_length


def _branch_bound(cities):
    best_order = []
    best_length = float('inf')

    for i in range(N_ITER):
        order = list(range(cities.shape[0]))
        shuffle(order)
        length = _calc_length(cities, order)
        start = time()

        changed = True
        while changed:

            changed = False

            for a in range(-1, cities.shape[0]):

                for b in range(a + 1, cities.shape[0]):

                    new_order = order[:a] + order[a:b][::-1] + order[b:]
                    new_length = _calc_length(cities, new_order)

                    if new_length < length:
                        length = new_length
                        order = new_order
                        changed = True

        if length < best_length:
            best_length = length
            best_order = order

    return best_order, best_length


if __name__ == "__main__":
    main()
