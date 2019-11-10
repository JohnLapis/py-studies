from sieve_of_erastosthenes import sieve
from Factorize import factorize

def mainn():
    primes = []
    for p in sieve(1000):
        primes.append((p,0))
    primes = dict(primes)
    
    for n in range (2,1000):
        if str(n)[-1] == '0':
            continue
        for f in factorize(n):
            primes[f[0]] += f[1] * n

    s = 1
    for p in primes:
        s += p**primes[p]

    return str(s)[-10:]


def main():
    s = 1
    for n in range(2,1000):
        if str(n)[-1] == '0':
            continue
        s += n**n

    return str(s)[-10:]

    
if __name__ == '__main__':
    print(main())
