nameString = input().split()
a = int(nameString[0])
k = int(nameString[1])
n = int(nameString[2])

bFirst = k - (a % k)
n -= a
check = False
while bFirst <= n:
    print(bFirst, end=' ')
    bFirst += k
    check = True

if check == False:
    print(-1)
