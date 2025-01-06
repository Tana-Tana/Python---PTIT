import math
def Check(number):
    number_list = number[len(number)-4:]
    xau = ''.join(number_list)
    if SNT(int(xau)) == True: return True
    return False

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