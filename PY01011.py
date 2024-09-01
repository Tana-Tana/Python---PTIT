def CheckBeautiNumber(m):
    n = m
    arr = [0] * 10
    while n > 0:
        if isinstance(n % 10, int) == True:
            arr[n % 10] = 1
            if n % 10 != 0 and n % 10 != 2 and n % 10 != 4 and n % 10 != 6 and n % 10 != 8:
                return False
            else:
                break
    cnt = 0
    for i in range(0, 10):
        if arr[i] > 0:
            cnt += 1
    if cnt % 2 == 1:
        return True
    else:
        return False


test = int(input())
while test > 0:
    number = int(input())
    for j in range(22, number):
        if CheckBeautiNumber(j) == True:
            print(j, end=' ')
    print()
    test -= 1
