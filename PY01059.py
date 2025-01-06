def YC1(number):
    res = 0
    for i in range(len(number)):
        if i%2 == 0:
            res += int(number[i])
    return res

def YC2(number):
    res = 1
    check = 1
    for i in range(len(number)):
        if i%2 == 1:
            if int(number[i]) == 0: continue
            res *= int(number[i])
            check = 0

    if check == 1: res = 0
    return res

if __name__ == "__main__":
    test = int(input())
    while test > 0:
        test -=1
        number = input()
        print(YC1(number),YC2(number))