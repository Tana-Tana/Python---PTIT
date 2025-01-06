def Check(arr1, arr2):
    arr1.sort()
    arr2.sort()
    for i in range(len(arr1)):
        if arr1[i] > arr2[i]: return False
    return True
#main
test = int(input())
while test > 0:
    test -= 1
    n = input()
    arr1 = [int(i) for i in input().split()]
    arr2 = [int(i) for i in input().split()]
    if Check(arr1,arr2): print("YES")
    else: print("NO")