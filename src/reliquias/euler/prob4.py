def main():
    for n in range(999,899,-1):
        for m in range(n,899,-1):
            p = str(m*n)
            if p == p[::-1]:
                return p


if __name__ == '__main__':
    print(main())
