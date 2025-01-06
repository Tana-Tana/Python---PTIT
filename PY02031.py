from math import *
def snt(number):
    if number < 2: return False
    for i in range(2,isqrt(number) + 1):
        if number % i == 0: return False
    return True

#main
n,m = map(int, input().split())
res = []
for i in range(n):
    arr = [int(i) for i in input().split()]
    res.append(arr)

for i in range(n):
    for j in range(len(res[i])):
        if snt(res[i][j]): res[i][j] = 1 
        else: res[i][j] = 0

#in
for i in range(n):
    current_list = res[i]
    for j in current_list: print(j,end = ' ')
    print()