def check(number):
    while number != 0:
        if(number%10 != 4) and (number%10!=7): return False
        number//=10
    return True

if __name__ == '__main__':
    test = int(input())
    while test > 0:
        test -= 1
        number = int(input())
        if check(number) == True: print("YES")
        else: print("NO")