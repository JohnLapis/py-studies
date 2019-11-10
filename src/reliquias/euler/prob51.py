from sieve_of_erastosthenes import sieve
from itertools import combinations


def f(string):
    #returns the positions of the repeating digits
    pos = ''
    for c in string:
        if string.count(c) > 1 :
            x = c
            break
    for i in range(len(string)):
        if string[i] == x:
            pos += str(i)
    return pos    

def r(string):
    #checks if a digit repeats
    for c in string:
        #if 2 digits are to be replaced, this should be a 1
        if string.count(c) > 2:
            return True
    
def main():
    primes = {}
    #for numbers below 100000, '0123' is to be used since
    #the last digit isn't to be changed in a 8 prime value family
    #the digit 3 is for the number of digits to be replaced
    for c in combinations('01234',3): 
        primes[''.join(c)] = []

    for p in sieve(1000000,100000):
        p = str(p)
        if r(p[:-1]):
            for c in combinations(f(p[:-1]),3):
                primes[''.join(c)] += [p]
                
    #dict for grouping numbers from the same family
    pp = {}
    for i in primes.items():
        for j in i[1]:
            j2 = list(j)
            for k in i[0]:
                j2[int(k)] = 'x'

            j2 = ''.join(j2)
            try:
                pp[j2] += [j]
            except KeyError:
                pp[j2] = [j]

    for i in pp.items():
        if len(i[1]) == 8:
            return i


if __name__ == '__main__':
    print(main())
