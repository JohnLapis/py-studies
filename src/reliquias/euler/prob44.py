from math import sqrt
from itertools import combinations


def p(n):
    return n*(3*n - 1)/2

def ispen(n):
    try:
        return (1 + sqrt(1 + 24*n))/2 % 3 == 0
    except:
        return False


def main():
    l = []
    o=[]
    for x in combinations(range(1,1000),2):
        j = x[0]
        k = x[1]
        if ispen(p(j) + p(k)) and  ispen(p(k) - p(j)):
            l.append([j,k,j-k])
        if ispen(p(k) - p(j)):
            o.append([j,k])
                
    return l,o


if __name__ == '__main__':
    l,o = main()
    for i in l:
        print(i,'aaaa')
    a=input()
    for i in o:
        print(i)
