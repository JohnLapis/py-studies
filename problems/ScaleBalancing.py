def ScaleBalancing(strArr): 
    a = strArr[0][0]
    b = strArr[0][1]
    for n in strArr[1]:
        if n + a == b or n + b == a:
            return str(n)
        for m in strArr[1]:
            if m == n:
                continue
            elif abs(m - n) == abs(a - b):
                if m + a == n + b:
                    return f'{m},{n}'
                else:
                    return f'{n},{m}'
            elif m + n == abs(a-b):
                return f'{m},{n}'
                    
print(ScaleBalancing([[3, 4], [1, 2, 7, 7]]))
print(ScaleBalancing([[13, 4], [1, 2, 3, 6, 14]]))
