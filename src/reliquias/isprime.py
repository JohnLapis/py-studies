from sieve_of_erastosthenes import sieve
from math import sqrt


def isprime(n, primes=[]):
    if n < 2:
        return False

    if not primes:
       primes = sieve(int(sqrt(n))) 
    
    for prime in primes:
        if n % prime == 0 and prime != n:
            return False
        if prime > sqrt(n):
            break

    return True


if __name__ == '__main__':
    print(isprime(int(input("Number: "))))
