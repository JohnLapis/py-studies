def main():
    """
    1- The first number has to be a 1; so, there has to be a 2
    so, there has to be a 4 and 8.
    2- When multiplying by 5, there will be a 5 or 0;
    hence, there has to be at least 5 digits
    3- By multiplying by 6, at least 3 numbers will exceed 10;
    so, assuming 1 becomes 2, there will be at least more 2 odd numbers,
    which means that there has to be 6 digits and one of them has to be a 5
    """

    for n in range(123456, 165432):
        if '5' not in str(n):
            continue
        if [sorted(str(n*i)) for i in range(1,7)].count(sorted(str(n))) == 6:
            return n

            
if __name__ == '__main__':
    print(main())
