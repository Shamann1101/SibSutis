from random import random


def calculate(pool, strat_a, strat_b, limit=100):
    summ = 0
    for iteration in range(limit):
        first_num = random()
        i = 0 if first_num < strat_a else 1
        second_num = random()
        j = 0 if second_num < strat_b else 1
        win = pool[i][j]
        summ += win
        print(f'Game #{iteration+1}\tNumber A: {first_num}\tStrategy A: {i}\tNumber B: {second_num}\tStrategy B: {j}\t'
              f'Win: {win}\tSummary win: {summ}\tMid: {summ / (iteration+1)}')


def main():
    strat_a = 9/14
    strat_b = 1/7
    pool = [
        [11, 6],
        [9, 18]
    ]
    calculate(pool, strat_a, strat_b, 100)


if __name__ == '__main__':
    main()
