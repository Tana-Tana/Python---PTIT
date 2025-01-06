from math import *
def TinhTong(number):
    res = 0
    if number == 1: return 1
    i = 2
    while i <= int(isqrt(number)) + 1:
        cnt = 0
        if number % i == 0:
            while number % i == 0:
                cnt+=1
                number//=i
        res += (cnt * i)
        i+=1
    
    if number != 1: res += number
    return res

if __name__ == "__main__":
    test = int(input())
    sum = 0
    while test > 0:
        test -=1
        number = int(input())
        sum += TinhTong(number)
    print(sum)
