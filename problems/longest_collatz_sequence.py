
def sequence():
    max = 0, 1
    for N in range(2,10**6):
        steps = 0
        n = N
        
        while n != 1:
            if n % 2 == 0:
                n /= 2
            else:
                n = n*3 + 1
            steps += 1

        if steps > max[0]:
            max = steps, N
            print(max)

    return max


if __name__ == '__main__':
    print(sequence())
