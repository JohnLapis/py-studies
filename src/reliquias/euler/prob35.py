from sieve_of_erastosthenes import sieve
from isprime import isprime

def main(limit):
    n = 0
    primes = sieve(limit)
    for p in primes:
        i = 0
        p = str(p)
        p2 = p
        while isprime(int(p2), primes=primes):
            i += 1
            if p2 == p[-1] + p[0:-1]:
                break
            p2 = p2[1:] + p2[0]

        if i == len(p):
            n += 1

    if limit > 10:
        n += 1 #because 11 is an exception

    return n


if __name__ == '__main__':
    print(main(1000000))
