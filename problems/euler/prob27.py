from sieve_of_erastosthenes import sieve
from isprime import isprime


def main(alimit, blimit):
    """
If limit = 100, then |a| < 100
"""
    longest_seq = (0,0,0) #length, a, b

    primes = sieve(1000)
    if alimit % 2 == 0:
        v = 1
        
    for a in range(-alimit+v, alimit, 2):
        for b in primes:
            n = 0
            while isprime(n**2 + a*n + b):
                n += 1

            if n > longest_seq[0]:
                longest_seq = (n, a, b)

    return longest_seq


if __name__ == '__main__':
    print(main(1000, 1001))
    
