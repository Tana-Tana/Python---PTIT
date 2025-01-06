from math import *
from bisect import *

limit = int(isqrt(10**9))
# sàng ngto tới 1e9**0.5 => khoảng 1e4 +- 1 số nhỏ 
ngto_list = []
isPrime = [True] * (limit + 1)
for i in range (2,limit+1):
    if isPrime[i]:
        ngto_list.append(i**2)
        for j in range (i*i,limit + 1,i):
            isPrime[j] = False
# thỏa mãn có 9 ước thì có 2 TH
n = int(input())
res = []
cnt = 0 
#TH1: p**8 => kiểm tra số ngto mà p**8 <= n => đếm
for i in ngto_list:
    if res.count(i**4) == 0:
        if i**4 <= n: 
            cnt += 1
            res.append(i**4)
#TH2: p**2 * q**2 => kiểm tra cặp số ngto mà p!=q và kq <= n => đếm
# Duyệt mảng toàn số ngto
for i in ngto_list:
    number_check = n//i
    if number_check == 0: break
    #Tim so dau tien be hon hoac bang thang number_check => index
    index_number = bisect_left(ngto_list,number_check)
    for j in range(index_number):
        if (res.count(ngto_list[j] * i) == 0) and (ngto_list[j] != i):
            res.append(ngto_list[j] * i)
            cnt += 1

# #Với p, q là snt => có công thức tính ước số là (8+1) = 9 và (2+1)*(2+1) = 9
print(cnt)