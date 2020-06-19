import math

def e_extension():
    e = str(math.e)
    c = 0
    x = input('How many decimal places of e do you want to see? ')
    print(e[:x+2])
    return

e_extension()