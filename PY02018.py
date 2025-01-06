n = int(input())
arr = [int(i) for i in input().split()]
arr = sorted(arr)
check = 1
for i in range(n-1):
    if (arr[i] + 1) != arr[i+1]:
        check = 0
        print(arr[i] + 1)
        break
if check == 1: print(arr[n-1] + 1)