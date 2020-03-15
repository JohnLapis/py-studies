from Divisors import find_divisors as div


def red(f):
    div2 = div(f[1])
    for d in reversed(div(f[0])):
        if d in div2:
            return f[0]/d,f[1]/d

    return f


def main():
    c = 1
    for k in range(9,1001):
        f = (2,1)
        for i in range(1, k):
            f = (2*f[0] + f[1], f[0])
        f = (f[0]+f[1],f[0]) #this counts as one expansion

        if len(str(f[0])) > len(str(f[1])):
            c += 1

    return c

            
if __name__ == '__main__':
    print(main())
