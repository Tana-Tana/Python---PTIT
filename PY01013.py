import math


def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)+1), 1):
        if n % i == 0:
            return False
    return True


def isResult(m):
    cnt = 0

    while m > 0:
        if isinstance(m, int) == True:
            cnt += (m % 10)
            m /= 10
            m = math.floor(m)
        else:
            break

    if(isPrime(cnt) == True):
        return True
    else:

        return False


test = int(input())
while test > 0:
    nameString = input().split()
    a = int(nameString[0])
    b = int(nameString[1])
    c = math.gcd(a, b)

    if isResult(c):
        print("YES")
    else:
        print("NO")
    test -= 1
