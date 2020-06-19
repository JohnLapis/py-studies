from sieve_of_erastosthenes import sieve
from Factorize import factorize
from Divisors import find_divisors

def tt(n):
    return int(((n+1) * n) / 2)

max = 0
for i in range(10000,20000):
    n = tt(i)
    factors = factorize(n)
    divisors = find_divisors(factors)
    l = len(divisors)
    if l > max:
        max = l
        print(n, l)
    if l > 500:
        print('yyyyyyyyyyeaaaahhh')
        break
