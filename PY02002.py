
# fibo
limit = 93
fibo = [0] * limit
fibo[0] = 0
fibo[1] = 1
fibo[2] = 1
for i in range(3,limit):
    fibo[i] = fibo[i-1] + fibo[i-2]
#main
test = int(input())
while test > 0:
    test -= 1
    a,b = map(int,input().split())
    if a > b: a,b = b,a
    for i in range(a,b+1): print(fibo[i], end = ' ')
    print()