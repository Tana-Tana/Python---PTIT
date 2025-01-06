from math import *
def SNT(number):
    if number < 2: return False
    for i in range(2,isqrt(number)+1):
        if number%i == 0:return False
    return True

def Check(number):
    numberCheck = number[len(number)-4:]
    if SNT(int(numberCheck)): return True
    return False

if __name__ == "__main__":
    test = int(input())
    while test > 0:
        test -=1
        number = input()
        if Check(number) == True: print("YES")
        else: print("NO")