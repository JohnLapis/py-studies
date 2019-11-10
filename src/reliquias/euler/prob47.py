from Factorize import factorize


def main():
    for n in range(647,1000000):
        if len(factorize(n, keep_exp=False)) >= 4\
           and len(factorize(n+1, keep_exp=False)) >= 4\
           and len(factorize(n+2, keep_exp=False)) >= 4\
           and len(factorize(n+3, keep_exp=False)) >= 4:
            return n

        
if __name__ == '__main__':
    print(main())

