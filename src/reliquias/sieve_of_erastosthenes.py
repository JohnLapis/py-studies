def sieve(limit, dlimit=2):
    numbers_list = [True for _ in range(limit + 1)]
    numbers_list[0:1] = [False, False]
    for start in range(2, limit + 1):
        if numbers_list[start]:
            for i in range(2 * start, limit + 1, start):
                numbers_list[i] = False
    primes = []
    for i in range(dlimit, limit + 1):
        if numbers_list[i]:
            primes.append(i)
            
    return primes


if __name__ == '__main__':
    print(sieve(int(input('Limit: '))))


