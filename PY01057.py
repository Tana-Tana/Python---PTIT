from math import *
def SNT(number):
    if number < 2: return False
    for i in range(2,isqrt(number)+1):
        if number%i == 0:return False
    return True

def Check(number):
    for i in range(len(number)):
        if SNT(i):
            if not SNT(int(number[i])): return False
        else:
            if SNT(int(number[i])): return False

    return True

if __name__ == "__main__":
    test = int(input())
    while test > 0:
        test -=1
        number = input()
        if Check(number): print("YES")
        else: print("NO")