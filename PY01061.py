from math import *
def SN_T(number):
    if number < 2: return False
    for i in range(2,isqrt(number)+1):
        if number%i == 0:return False
    return True

def SNT(number):
    number_dau = number[:3]
    number_cuoi = number[len(number)-3:]
    if SN_T(int(number_dau)) == True and SN_T(int(number_cuoi)) == True: return True
    return False
if __name__ == "__main__":
    test = int(input())
    while test > 0:
        test -=1
        number = input()
        if SNT(number) == True: print("YES")
        else: print("NO")