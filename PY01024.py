import math


def Check(n):
    sum = int(n[0])
    for i in range(1, len(n)):
        if(abs(int(n[i]) - int(n[i-1]))) != 2:
            return False
        sum += int(n[i])
    if(sum % 10 == 0):
        return True
    else:
        return False


test = int(input())
while test > 0:
    test -= 1
    n = input()
    if(Check(n)):
        print("YES")
    else:
        print("NO")
