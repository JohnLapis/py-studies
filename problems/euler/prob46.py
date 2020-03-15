from sieve_of_erastosthenes import sieve
from math import sqrt


def main():
    primes = sieve(10000)
    for n in range(9,10000,2):
        if n in primes:
            continue
        for p in primes:
            if p > n:
                return n
            x = sqrt((n-p)/2)
            if int(x) == x:
                break
                

if __name__ == '__main__':
    print(main())
