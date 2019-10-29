from isprime import isprime


def main():
    l = []
    n = '11'
    while True:
        if n[0] in '2357' and n[-1] in '357' and '0' not in n and isprime(int(n)):
            if len(n) == 2:
                l.append(int(n))
            else:
                for i in range(2, len(n)):
                    if not isprime(int(n[:i])) or not isprime(int(n[-i:])):
                        break
                else:
                    l.append(int(n))
        if len(l) == 11:
            break
        n = str(int(n) + 2)

    return sum(l)
    

if __name__ == '__main__':
    print(main())
