from random import random


def calculate(pool, strat_a, strat_b, limit=100):
    summary = 0
    freq = list()
    for i in range(len(pool)):
        freq.append([0] * len(pool[0]))
    for iteration in range(limit):
        first_num = random()
        if first_num < strat_a:
            i = 0
        else:
            i = 1
        freq[0][i] += 1
        second_num = random()
        if second_num < strat_b:
            j = 0
        else:
            j = 1
        freq[1][j] += 1
        win = pool[i][j]
        summary += win
        # freq[i][j] += 1
        print(f'Game #{iteration+1}\tNumber A: {first_num}\tStrategy A: {i}\tNumber B: {second_num}\tStrategy B: {j}\t'
              f'Win: {win}\tsummary win: {summary}\tMid: {summary / (iteration+1)}')
    for i in range(len(freq)):
        for j in range(len(freq[i])):
            freq[i][j] /= limit
    print(f'Frequency: {freq}')


def main():
    strat_a = 9/14
    strat_b = 6/7
    pool = [
        [11, 6],
        [9, 18]
    ]
    calculate(pool, strat_a, strat_b, 100)


if __name__ == '__main__':
    main()
