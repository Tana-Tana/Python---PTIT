import math
def Check(number):
    cntNT = 0
    for i in number:
        if SNT(int(i)) == True: cntNT += 1
    if SNT(len(number)) == False: return False
    if 2*cntNT <= len(number): return False
    return True

def SNT(number):
    if number < 2: return False
    for i in range(2,math.isqrt(number) + 1):
        if number % i == 0 : return False
    return True


if __name__ == "__main__":
    test = int(input())
    while test > 0:
        test -= 1
        n = input()
        if Check(n) == True: print("YES")
        else: print("NO")