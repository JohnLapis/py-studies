from math import sqrt
from itertools import combinations


def ispen(x):
    return (sqrt(1 + 24*x) + 1) % 6 == 0

def main():
    """
    Checking the upper limit isn't feasible in my pc
    And the first occurence just happens to be the minimum D
    """
    d = 0
    for c in combinations([n*(3*n-1)/2 for n in range(1,10001)], 2):
        if c[0] == pj:
            continue
        if ispen(c[0] + c[1]) and ispen(c[1] - c[0]):
            if d == 0 or c[1] - c[0] < d:
                d = c[1]-c[0]
        
    return d


if __name__ == '__main__':
    print(main())
