from itertools import combinations
from functools import reduce
from Factorize import factorize


def find_divisors(n):
    factors = factorize(n)
    divisors = [(f[0],1) for f in factors]

    for i in range(2, len(factors)+1):
        divisors += [div for div in combinations([f[0] for f in factors], i)]

    for f in factors:
        if f[1] > 1:
            for div in divisors:
                if f[0] in div:
                    exp = f[1]
                    while exp > 1:
                        new_div = list(div) 
                        new_div[new_div.index(f[0])] = f[0] ** exp
                        divisors.append(new_div)
                        exp -= 1

    divisors = [reduce(lambda x,y: x*y, div) for div in divisors]

    divisors.append(1)
    return sorted(divisors)


if __name__ == '__main__':  
    print(find_divisors(int(input('here '))))
