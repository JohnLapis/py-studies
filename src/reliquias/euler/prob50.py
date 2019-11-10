from sieve_of_erastosthenes import sieve
from isprime import isprime


def main1():
    #47619 = 1.000.000 / 21
    n = 953
    m = 21
    primes = sieve(47618)
    for j in range(m,600,2):
        for i in range(len(primes)):
            p = sum(primes[i:i+1+j])
            if isprime(p) and p < 1000000:
                print(p)
                print(primes[i:i+1+j])
                #m += 2
                n = p
                
            if i + m > len(primes) or p > 999999:
                break
        print(j)

    return n


def main2():
    s = 0
    n = 953
    i=0
    m=0
    primes = sieve(47618)
    for i in range(len(primes)):
        s += primes[i]
        if s > 999999:
            break
        if isprime(s):
            print(s)
            n = s
            m = i+1
        else:
            for j in range(i):
                if i+1-j < m:
                    break
                s -= primes[j]
                if isprime(s):
                    n = s
                    m = i - j
                    break

    return n


if __name__ == '__main__':
    print(main2())
    
