n = int(input())
arr = [int(i) for i in input().split()]
current = arr[0]
cnt = 0
for i in range(1,len(arr)):
    if arr[i] != current: cnt+=1;current = arr[i]
print(cnt)