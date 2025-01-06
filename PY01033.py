from math import *
l,r = map(int, input().split())
for i in range(l,r+1):
    for j in range(i+1, r+1):
        for z in range (j+1,r+1):
            if (gcd(i,j) == 1) and (gcd(z,j) == 1) and(gcd(i,z) == 1): 
                print("(",i,", ",j,", ",z,")",sep = "")