def is_happynumber(n):
    suma = 0
    n = int(n)
    if n <= 0 and n - int(n) != 0:
        return False
    else:
        while len(str(n)) >  1:
            suma = sum([int(i)**2 for i in str(n)])
            n = str(suma)
        if suma == 1 or n == 1:
            return True
        else:
            return False

count = 0
j = 1
happy_numbers = []

while True:
    if(is_happynumber(j)):
        count += 1
        happy_numbers.append(j)
    if count == 8: break
    j += 1
print(happy_numbers)
