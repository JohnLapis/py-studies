from Factorize import factorize
from Divisors import find_divisors


def d(x):
    return sum(find_divisors(factorize(x))[:-1])

def sum_amicable(limit):

    amicables = []

    for n in range(2,limit+1):
        m = d(n)
        if m != n and d(m) == n:
            amicables.append(n)

    print(amicables)
    return sum(amicables)


if __name__ == '__main__':
    print(sum_amicable(10000))
