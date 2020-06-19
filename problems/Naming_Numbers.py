'''
Number Names - Show how to spell out a number in English. You can use a preexisting implementation or roll your own, but you should support inputs up to at least one million (or the maximum value of your language's default bounded integer type, if that's less). Optional: Support for inputs other than positive integers (like zero, negative integers, and floating-point numbers).

Coin Flip Simulation - Write some code that simulates flipping a single coin however many times the user decides. The code should record the outcomes and count the number of tails and heads.
'''
def name999(num, leng, t=False):
    name = []
    if t and num == '0': return name
    if leng == 1 or num[-2] == '0' and num[-1] != '0':
        name.append(n_list[0][int(num[-1])])
    elif num[-2] == '1':
        name.append(n_list[1][int(num[-1])])
    elif num[-2] > '1':
        name.append(n_list[int(num[-2])])
        if num[-1] != '0':
            name[0] += '-' + n_list[0][int(num[-1])]
    if leng > 2 and num[-3] != 0:
        name.append(n_list[0][int(num[-3])] + ' ' + special_names[0])
    return name

def find_num_name(num):
    if not num.isdecimal() or int(num) > 999999:
        raise ValueError
    if len(num) <= 3:
        name = name999(num, len(num))
    else:
        name = name999(str(int(num[-3:])), len(str(int(num[-3:]))), True)
        name.append(special_names[1])
        thousands = name999(num[:-3], len(str(int(num[:-3]))))
        for i in thousands:
            name.append(i)
    return ' '.join(list(reversed(name)))

n_list = [
    ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'], ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen'], 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
special_names = ['hundred', 'thousand']

if __name__ == '__main__':
    print(find_num_name(input()))
