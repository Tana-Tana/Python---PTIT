from itertools import *

n,k = map(int, input().split())
res = list(map(int,input().split()))
# tach thanh 1 chuoi chi co cac so khac nhau
list_n = []
for i in res:
    if list_n.count(str(i)) == 0: list_n.append(str(i))

# sap xep
list_n.sort(key = lambda x : int(x))
# print(list_n)

combinations_res = combinations(list_n,k)
for i in combinations_res: 
    print(' '.join(i))
    