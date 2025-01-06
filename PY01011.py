
def CheckSTN(number1):
    number = list(number1)
    l = 0
    r = len(number)-1
    while l <= r:
        if number[l] != number[r]: return False
        if (number[l] != "0") and (number[l] != "2") and(number[l] != "4") and(number[l] != "6") and(number[l] != "8"): return False
        if (number[r] != "0") and (number[r] != "2") and(number[r] != "4") and(number[r] != "6") and(number[r] != "8"): return False
        l+=1
        r-=1
    if len(number) % 2 == 1: return False
    return True

if __name__ == '__main__':
    test = int(input())
    while test > 0:
        test -= 1
        number = int(input())
        for i in range(22, number,22):
            if CheckSTN(str(i)) == True: print(i, end = ' ')
        print()

