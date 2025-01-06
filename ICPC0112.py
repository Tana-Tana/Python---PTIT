from math import *

# ham dem cac cap so < n 
def tinh_toan(number):
    cnt = 0
    for i in range(6,number):
        if isPrime[i] == True and isPrime[i-6] == True and ((isPrime[i-2] == True) or (isPrime[i-4] == True)): cnt+=1
    return cnt

#sang nguyen to
limit = 1000000
isPrime = [True] * (limit+100)
isPrime[0] = isPrime[1] = False
for i in range(2,isqrt(limit) + 1):
    if isPrime[i]:
        for j in range(i*i,limit + 100,i):
            isPrime[j] = False

#main
test = int(input())
while test > 0:
    test -= 1
    number = int(input())
    print(tinh_toan(number))
