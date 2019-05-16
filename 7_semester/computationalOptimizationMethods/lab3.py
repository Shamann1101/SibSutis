FREQUENCY = 0.0001


list_alpha = list()
list_x = list()


gx1, gx2 = 5, 6


def fx1(x1):
    return -2 * x1 + 8


def fx2(x2):
    return -2 * x2 + 6


def get_g(x):
    return 5 * x[0] + 6 * x[1] - 60


# TODO: Need to unset double alpha
def get_alpha(k):
    alpha = [0, 0]
    g = get_g(list_x[k-1])
    if g < 0:
        alpha[0] = list_alpha[k-1][0] - 0.1 * g
        alpha[1] = list_alpha[k-1][1] - 0.1 * g
    list_alpha.append(alpha)
    return alpha


def get_x(k):
    x = list_x[k-1]
    alpha = get_alpha(k)
    x1 = max(0, x[0] + 0.1 * (fx1(x[0]) + alpha[0] * gx1))
    x2 = max(0, x[1] + 0.1 * (fx2(x[1]) + alpha[1] * gx2))
    print(f'{x[0]} + {0.1} * ({fx1(x[0])} + {alpha[0]} * {gx1}) = {x1}')
    print(f'{x[1]} + {0.1} * ({fx2(x[1])} + {alpha[1]} * {gx2}) = {x2}')
    list_x.append([x1, x2])
    print(get_f(k))
    print()
    return list_x[k]


def get_f(k):
    return -(list_x[k][0] - 4) ** 2 - (list_x[k][1] - 3) ** 2


def main():
    list_alpha.append([0, 0])
    list_x.append([6, 5])
    # list_x.append([10, 10])
    # print(get_alpha(1))
    # print(get_x(1))

    i = 1
    while True:
        x = get_x(i)
        if get_f(i) - get_f(i-1) < FREQUENCY and get_g(list_x[i]) > 0:
            print(x)
            print(f'g: {get_g(list_x[i])}')
            print(get_f(i))
            break

        i += 1
        # if i == 100:
        #     break


if __name__ == '__main__':
    main()
