from itertools import permutations, combinations_with_replacement


def main():
    """
Any number containing a '7' wouldn't be valid since
7^5 > 9999 and 6^5 > 6000
"""
    total = []
    for number in combinations_with_replacement('0123456789', 6):
        s = sum([int(digit)**5 for digit in number])
        for p in set(permutations(''.join(number))):
            if int(''.join(p)) == s:
                total.append(s)
                break


    return sum(total)

if __name__ == '__main__':
    print(main())
