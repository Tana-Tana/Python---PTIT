n = int(input())
arr = [float(i) for i in input().split()]
max_number = max(arr)
for i in arr: 
    if i == max_number: arr.remove(i)
min_number = min(arr)
for i in arr:
    if i == min_number: arr.remove(i)
print('{:.2f}'.format(sum(arr)/len(arr)))