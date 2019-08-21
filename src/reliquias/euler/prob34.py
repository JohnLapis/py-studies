from math import factorial as fac


def main():
    s = 0
    for n in range(10, 9999999):
        if sum([fac(int(d)) for d in str(n)]) == n:
            s += n
            print(n)

    return s


if __name__ == '__main__':
    print(main())
