def lahn(cc):
    if len(cc) != 16:
        return False
    a = [int(x)**2 for n in cc[1:15:2]] if x < 5 else x - 9
    
if __name__ == '__main__':
    lahn(int(input("Enter Credit Card number: "))
