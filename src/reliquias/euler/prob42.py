from math import sqrt


def main(l):
    n = 0
    for w in l:
        if sqrt(1 + 8*sum([ord(c)-64 for c in w])) % 2 != 0:
            n += 1

    return n


if __name__ == '__main__':
    with open('./files/p042_words.txt', 'r') as f:
        print(main(f.read().replace('"', '').split(',')))
