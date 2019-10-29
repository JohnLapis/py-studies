from sieve_of_erastosthenes import sieve
from math import sqrt


def isprime(n, primes=[]):
    if n < 2:
        return False

    if not primes:
       for prime in sieve(int(sqrt(n))):
           if n % prime == 0:
               return False
    else:
        for prime in primes:
            if n % prime == 0:
                return False
            if prime > sqrt(n):
                break
        
    return True


if __name__ == '__main__':
    print(isprime(int(input("Number: "))))
