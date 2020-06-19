import math

def fib(limit):
        if limit > 1000000:
		i = int(input('The number passes the limit. Enter a valid number: '))

	a, b = 1, 1
        fib_list = [1,1]
        for n in range(limit):
                c = a + b
                a, b = b, c
                fib_list.append(c)

        return fib_list


if __name__ == '__main__':
        print(fib(int(input('How many numbers of the the Fibonacci sequence do you want to generate? '))))
