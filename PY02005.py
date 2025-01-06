n = int(input())
arr = [int(i) for i in input().split()]
cnt = 0
for i in range(n):
    for j in range(i+1,n):
        if arr[i] > arr[j]: cnt+=1
print(cnt)