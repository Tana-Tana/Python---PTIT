from math import *
test = int(input())
while test > 0:
    test -= 1
    number = input()
    sum = 0
    for i in number:
        sum += factorial(int(i))
    if sum == int(number): print("Yes")
    else: print("No")
