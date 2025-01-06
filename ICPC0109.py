#TLE vi O(n/2)
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
    a,b,c = 100000001, 100000001, 100000001
    #Tim a
    index = -1
    l,r = 0,(len(arr)-1)
    while l<=r:
        if arr[l] < a:
            index = l
            a = arr[l]
        if arr[r] < a:
            index = r
            a = arr[r]
        l+=1
        r-=1
    #Tim b
    index_b = -1
    l,r = 0,len(arr)-1
    while l<=r:
        if arr[l] < b and b >= a and index != l:
            index_b = l
            b = arr[l]
        if arr[r] < b and b >= a and index != r:
            index_b = r
            b = arr[r]
        l+=1
        r-=1
    
    l,r = 0,len(arr)-1
    while l<=r:
        if arr[l] < c and c >= b >= a and index != l != index_b:
            c = arr[l]
        if arr[r] < c and c >= b >= a and index != r != index_b:
            c = arr[r]
        l+=1
        r-=1
    
    print(a+b+c)

