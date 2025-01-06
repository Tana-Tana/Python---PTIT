from math import *

if __name__ == "__main__":
    test = int(input())
    while test > 0:
        test -= 1
        number = int(input())
        print(1,end = ' ')
        i = 2
        while i <= isqrt(number) + 1:
            if number % i == 0:
                cnt = 0
                while number%i == 0:
                    number//=i
                    cnt+=1
                print("* ",i,"^",cnt,sep = '', end = ' ')
            i+=1
        if(number != 1): print("* ",number,'^',1,sep = '', end = '\n') 
        else: print()