from math import *

test = int(input())
while test > 0:
    test -= 1
    n  = input()
    nDao = n[::-1]
    if gcd(int(n),int(nDao)) == 1: print("YES")
    else: print("NO") 