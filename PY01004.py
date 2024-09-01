import math


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


test = int(input())
while test > 0:
    k = int(input())
    cnt = 0
    for i in range(1, k):
        if math.gcd(k, i) == 1:
            cnt += 1
    if is_prime(cnt) == True:
        print("YES")
    else:
        print("NO")
    test -= 1
