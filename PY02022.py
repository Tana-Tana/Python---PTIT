from math import *
def snt(number):
    if number < 2: return False
    for i in range(2,isqrt(number) + 1):
        if number % i == 0: return False
    return True

#main
n = int(input())
arr = [int(i) for i in input().split()]
dict_res = {}
for i in arr:
    if snt(i):
        if not (i in dict_res): dict_res[i] = 1
        else: dict_res[i] +=1
for key, value in dict_res.items():
    print(key,value)