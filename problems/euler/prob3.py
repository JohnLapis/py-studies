from Factorize import factorize


for nn in range (399993, 310013, -10010):
    for pp in range (nn, nn - 10000, -1100):
        #    n = int(input('e '))
        o = 1
        n = pp
        a = factorize(n)
        if not isinstance(a, list):
            continue
        print(n)        
        print(a)
        for i in a:
            o *= i
        print(n / o, o)
        print('-----------------------------------------')

for pp in range (309903, 300003, -1100):
        #    n = int(input('e '))
        o = 1
        n = pp
        a = factorize(n)
        if not isinstance(a, list):
            continue
        print(n)
        print(a)
        for i in a:
            o *= i
        print(n / o, o)
        print('-----------------------------------------')
        
#do at least from 300003 to 799997
