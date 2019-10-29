from itertools import permutations

def main():
    s = 0
    for n in permutations('1234567890'):
        if n[0] == '0':
            break
        if n[5] not in '5':
            """ 
            '0' doesn't count as any number divisible by 11
            and starting with '0' would have repeated digits
            """
            continue
        if n[3] not in '02468':
            continue
        
        n = ''.join(n)
        if int(n[2:5]) % 3 != 0:
            continue
        if int(n[4:7]) % 7 != 0:
            continue
        if int(n[5:8]) % 11 != 0:
            continue
        if int(n[6:9]) % 13 != 0:
            continue
        if int(n[7:]) % 17 != 0:
            continue

        s += int(n)

    return s


if __name__ == '__main__':
    print(main())
