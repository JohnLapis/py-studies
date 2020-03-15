def ispal(n):
    return n == n[-1::-1]

def main(limit):
    s = 0
    for n in range(limit):
        if ispal(str(n)) and ispal(bin(n)[2:]):
            s += n

    return s


if __name__ == '__main__':
    print(main(1000000))
