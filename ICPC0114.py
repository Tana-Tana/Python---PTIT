from math import *
def snt(number):
    if number < 2 : return False
    for i in range(2,isqrt(number) + 1):
        if number % i == 0: return False
    return True
def Check(number):
    if not snt(number): return False
    if not snt(int(str(number)[::-1])): return False
    list_number = []
    while number!=0:
        list_number.append(number%10)
        number//=10
    if not snt(sum(list_number)): return False
    for i in range(len(list_number)):
        if  (list_number[i] != 2) and  (list_number[i] != 3) and  (list_number[i] != 5) and  (list_number[i] != 7): return False
    return True
#main
test = int(input())
while test > 0:
    test -= 1
    number = int(input())
    if Check(number): print("Yes")
    else: print("No")