from math import *
def SN_T(number):
    if number < 2: return False
    for i in range(2,isqrt(number)+1):
        if number%i == 0:return False
    return True

def Check(number):
    if SN_T(len(number)) == False: return False
    cnt = 0
    for i in number:
        if SN_T(int(i)) == True: cnt+=1
    
    if 2*cnt <= len(number): return False
    return True
if __name__ == "__main__":
    test = int(input())
    while test > 0:
        test -=1
        number = input()
        if Check(number) == True: print("YES")
        else: print("NO")
