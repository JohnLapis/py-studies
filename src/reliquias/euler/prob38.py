from itertools import permutations


def main():
    for n in permutations('8765432',3):
        n = '9'+''.join(n)
        n += str(int(n)*2)
        if ''.join(sorted(n)) == '123456789':
            return n


if __name__ == '__main__':
    print(main())
