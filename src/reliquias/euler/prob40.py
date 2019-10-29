def main():
    p = 1
    i = 1
    n = '1'
    k = 1
    while True:
        if len(n) >= 10**k:
            p *= int(n[10**k-1])
            k += 1
            if k > 9:
                break

        i += 1
        n += str(i)
    return p
    
if __name__ == '__main__':
    print(main())
