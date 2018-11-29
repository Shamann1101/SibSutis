def parentheses(widths):
	print("widths:", widths)
	res = dict()
	n = len(widths) - 1
	for i in range(n):
		res[i, i] = 0
	for t in range(n):
		if t == 0:
			continue
		for k in range(n - t):
			j = k
			values = []
			while j < k+t:
				value = res[k, j] + res[j+1, k+t] + widths[k] * widths[j+1] * widths[k+t+1]
				values.append(value)
				print(f'f({k}, {k+t}) = f({k},{j}) + f({j+1},{k+t}) + {widths[k]} * {widths[j+1]} * {widths[k+t+1]} = {value}')
				j += 1
			res[k, k+t] = min(values)
	print(res)


def main():
	widths = [10, 20, 50, 1, 100]
	parentheses(widths)


if __name__ == '__main__':
    main()
