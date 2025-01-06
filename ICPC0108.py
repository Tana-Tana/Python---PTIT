test = int(input())
while test > 0:
    test -= 1
    n = int(input())
    arr = [int(i) for i in input().split()]
    arr.sort()
    cnt = 0
    for i in range(n-2):
        l = i + 1
        r = n-1
        while l < r:
            if arr[l] + arr[r] + arr[i] == 0:
                l+=1
                cnt+=1
            elif arr[l] + arr[r] + arr[i] > 0:
                r-=1
            else: l+=1
    print(cnt)
