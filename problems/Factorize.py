from sieve_of_erastosthenes import sieve
from math import sqrt


def factorize(N, limit=None, keep_exp=True):

    if N < 2:
        return [(N,1)]

    if limit == None:
        limit = int(sqrt(N))

    n = N
    primes = sieve(limit)
    factors = []

    if keep_exp == True:
        for prime in primes:
            if n % prime == 0:
                i = 0
                while n % prime == 0:
                    n /= prime
                    i += 1
                factors.append((prime, i))
                if n == 1:
                    break
        if n != 1:
            factors.append((int(n), 1))
    else:
        for prime in primes:
            if n % prime == 0:
                factors.append(prime)
                while n % prime == 0:
                    n /= prime
                if n == 1:
                    break
        if n != 1:
            factors.append(int(n))

    return factors


if __name__ == '__main__':
    print(factorize(int(input('Number: '))))
