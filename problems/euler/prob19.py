
def main():
    sundays = 0
    # 1=sunday, 2=monday, etc.
    months = [3, 6, 6, 2, 4, 7, 2, 5, 1, 3, 6, 1] #from year 1901

    for y in range(1901,2000):
        if y % 4 == 0:
            months[2:] = [d+1 for d in months[2:]]

        for i in range(12):
            if months[i] > 7:
                months[i] -= 7    
        sundays += months.count(1)

        if y % 4 == 0:
            months = [d+2 for d in months]
        else:
            months = [d+1 for d in months]


    #2000 is handled separately to avoid unnecessary checks
    sundays += months.count(1)

    return sundays
    

if __name__ == '__main__':
    print(main())
