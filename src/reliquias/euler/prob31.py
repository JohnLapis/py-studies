from math import factorial as fac


def comb_with_rep(n,r):
    print(n,r,'aa')
    n = int(n)
    r = int(r)
    d = 1
    for i in range(n-1+r, n-1, -1):
        d *= i

    return d/fac(r)

def main(value, coins):
    print(value, coins)
    if value == 1:
        return 1
    if not coins:
        return 1
    coins = sorted(coins)
    n = value / coins[-1]
    if n == 1:
        print('a')
        return main(coins[-1], coins[:-1]) + 1
    elif n == int(n):
        print('b')
        return comb_with_rep(main(coins[-1], coins), n)
    else:
        print('c')
        return comb_with_rep(main(coins[-1], coins), int(n))\
    * main((n - int(n))*coins[-1], coins[:-1])


if __name__ == '__main__':
    u=main(200, [1,2,5,10,20,50,100,200])
    i=u/5
    print(i)
