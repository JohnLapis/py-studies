def comb(n,r):
    c = 1
    if n-r>r:
        a, b = n-r, r
    else:
        b, a = n-r, r
        
    for i in range(a+1,n+1):
        c *= i

    for i in range(2,b+1):
        c /= i

    return c

    
def main():
    ways = 0
    for n in range(1,101):
        for r in range(n):
            if comb(n,r) > 1000000:
                ways += 1

    return ways


if __name__ == '__main__':
    print(main())
