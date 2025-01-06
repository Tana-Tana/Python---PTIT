test = int(input())
while test > 0:
    test -= 1
    n = int(input())
    arr = {}
    while n > 0:
        n-=1
        number = int(input())
        if not (number in arr): arr[number] = 1
        else: arr[number] += 1
    arr = dict(sorted(arr.items(), key = lambda x : (-x[1],x[0])))
    for i in arr.keys():
        print(i)
        break
    