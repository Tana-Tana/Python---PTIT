from math import *
if __name__ == "__main__":
    test = int(input())
    while test > 0:
        test -=1
        number_1 = int(input())
        number_2 = int(input())
        print(gcd(number_1,number_2))