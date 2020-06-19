def main(limit):
    numbers = [i for i in range(limit + 1)]
    # 1 and 0 aren't primes
    numbers[0:2] = [False, False]

    for i in range(2, limit + 1):
        if numbers[i]:
            for x in range(i * 2, limit + 1, i):
                numbers[x] = 0

    return [n for n in numbers if n]


if __name__ == '__main__':
    primes = main(int(input('Limit for primes: ')))
    print(primes)


