from math import *
test = int(input())
while test > 0:
    test -= 1
    n = int(input())
    arr = [int(i) for i in input().split()]
    a = []
    res = [0] * (n+1)
    for  i in range(n):
        while len(a) > 0 and arr[i] >= arr[a[-1]]: a.pop()
        if len(a) == 0: print(i+1, end = ' ')
        else: print(i - a[-1], end = ' ')
        a.append(i)
    print()
        