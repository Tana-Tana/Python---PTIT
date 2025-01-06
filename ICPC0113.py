#sang nguyen to
from math import *
isPrime = [True] * (int(1e6)+1)
isPrime[0] = isPrime[1] = False
for i in range(2,isqrt(int(1e6)) + 1):
    if isPrime[i]:
        for j in range(i*i,int(1e6) + 1, i):
            isPrime[j] = False

#main
test = int(input())
while test > 0:
    test -= 1
    n = int(input())
    res  = []
    for i in range(n):
        if isPrime[i]:
            if int(str(i)[::-1]) != i and int(str(i)[::-1]) < n and isPrime[int(str(i)[::-1])] and res.count(i) == 0: print(i,str(i)[::-1],end = ' '); res.append(i);res.append(int(str(i)[::-1]))
    print()