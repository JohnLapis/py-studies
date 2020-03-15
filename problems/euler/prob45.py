from math import sqrt


def main():
    n = 147
    x = n*(2*n-1)
    while (sqrt(1 + 24*x)+1) % 6 != 0:
        n += 1
        x = n*(2*n-1)
    
    return x


if __name__ == '__main__':
    print(main())
