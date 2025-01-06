from math import *
def isPrime(number):
    if number < 2: return False
    for i in range(2,isqrt(number)+1):
        if(number % i == 0) : return False
    return True

if __name__ == "__main__":
    test = int(input())
    while test > 0:
        test -=1
        a,b = map(int, input().split())
        res = gcd(a,b)
        # print(res)
        # tinh tong chu so
        tong = 0
        while res != 0:
            tong += (res % 10)
            res//=10
        
        if(isPrime(tong) == True): print("YES")
        else : print("NO")
        