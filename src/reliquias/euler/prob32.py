from itertools import permutations


def main():
    """
10,000 (smallest 5-digit number) > 9*999 and 99*99.
999 (largest 3-digt number) < 111*111, 11*1111 and 1*11111
Therefore, the product will have 4 digits
"""
    s = []
    #p will be split into the multiplicand and multiplier
    for d in permutations('123456789', 5):
        d = ''.join(d)
        prod = str(int(d[0]) * int(d[1:]))
        if '0' not in prod and len(prod) == 4 and len(set(prod + d)) == 9:
            s.append(int(prod))
        else:
            prod = str(int(d[:2]) * int(d[2:]))
            if '0' not in prod and len(prod) == 4 and len(set(prod + d)) == 9:
                s.append(int(prod))

    return sum([n for n in set(s)])
                    

if __name__ == '__main__':
    print(main())
