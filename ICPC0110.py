# code MLE chua khac phuc
test = int(input())
while test > 0:
    test -= 1
    n = int(input())
    arr = list(map(int,input().split()))
    if len(arr) == 1: 
        print(arr[0])
        continue
    if len(arr) == 2:
        print(arr[0] + arr[1])
        continue
    a,b,c = -1e9,-1e9,-1e9
    index = -1
    for i in range(len(arr)):
        if a < arr[i]: a = arr[i]; index = i
    index_b = -1
    for i in range(len(arr)):
        if (b < arr[i]) and (b <= a) and (index != i): b = arr[i]; index_b = i
    for i in range(len(arr)):
        if (c < arr[i]) and (c<=b<=a) and (index != i != index_b): c = arr[i]
    print(a+b+c)

