from sieve_of_erastosthenes import sieve
from itertools import combinations


def ll(l):
    #checks if there can be formed an A.P. from a list of any length
    for c in combinations(l,3):
        if c[1] - c[0] == c[2] - c[1]:
            return c


def main(low_limit, up_limit):
    primes = []
    for p in sieve(up_limit):
        if p < low_limit:
            continue
        primes.append(p)

    _primes = list(primes)
    #all permutations of primes that appear more than 3 times within the limit
    lp = set()
    for i in range(len(_primes)):
        _primes[i] = ''.join(sorted(str(_primes[i])))
    for p in _primes:
        if _primes.count(p) >= 3:
            lp.add(p)

    #dictionary with the primes that are permutations of one another
    oo = {}
    for i in lp:
        oo[i] = []
    for p in primes:
        if ''.join(sorted(str(p))) in lp:
            oo[''.join(sorted(str(p)))] = oo[''.join(sorted(str(p)))] + [p]

    for i in oo.items():
        numbers = ll(i[1])
        if numbers and 1487 not in numbers:
            return numbers


if __name__ == '__main__':
    print(main(1000,9999))
