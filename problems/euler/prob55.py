def ispal(n):
    return l


def main():
    l = 0
    d = {}
    for n in range(9999,0,-1):
        N = n
        for i in range(1,50):
            try:
                if d[n] + i < 50:
                    d[N] = d[n] + i
                    break
                else:
                    d[N] = 50
                    l += 1
                    break
            except:
                n = int(str(n)[-1::-1]) + n
                if str(n) == str(n)[-1::-1]:
                    d[N] = i
                    break
        else:
            d[N] = 50
            l += 1

    return l
    

if __name__ == '__main__':
    print(main())
