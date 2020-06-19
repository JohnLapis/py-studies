import math

def pi_extension():
    pi = str(math.tau/2)
    c = 0
    x = input('How many decimal places of PI do you want to see? ')
    print(pi[:x+2])
    return

pi_extension()