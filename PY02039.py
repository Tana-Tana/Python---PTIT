n = int(input())
res = []
for i in range(n):
    arr = [int(i) for i in input().split()]
    res.append(arr)

sum_nua_tren = 0
for i in range(n):
    for j in range(i+1,len(res[i])):
        sum_nua_tren += res[i][j]

sum_nua_duoi = 0
for i in range(n-1,-1,-1):
    for j in range(i-1, -1, -1):
        sum_nua_duoi += res[i][j]

k = int(input())
if abs(sum_nua_tren - sum_nua_duoi) <= k: print('YES',abs(sum_nua_tren - sum_nua_duoi),sep = '\n')
else: print('NO',abs(sum_nua_tren - sum_nua_duoi),sep = '\n')
