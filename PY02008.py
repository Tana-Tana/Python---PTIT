from math import *
def snt(number):
    if number < 2: return False
    for i in range(2,isqrt(number) + 1):
        if number%i==0: return False
    return True
#main
n,x = map(int, input().split())
print(x,end=' ')
cnt = 2
for i in range(n):
    while not snt(cnt): cnt+=1
    print(x+cnt, end = ' ')
    x += cnt
    cnt += 1
 