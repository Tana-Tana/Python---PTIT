from math import *

def SoNguyenTo(number):
    if number < 2: return False
    for i in range(2,isqrt(number)+1):
        if number % i == 0: return False
    return True

if __name__ == '__main__':
    test = int(input())
    while test > 0 :
        test -=1
        cnt = 0
        n = int(input())
        for i in range(1,n): 
            if gcd(n,i)==1: cnt+=1
        if SoNguyenTo(cnt) == True: print("YES")
        else: print("NO")