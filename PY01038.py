def TinhToan(number):
    if int(number) % 7 == 0:
        return number
    for i in range(1000):
        number_dao = number[::-1]
        res = int(number) + int(number_dao)
        if res % 7 == 0:
            return res
        number = str(res)
    return -1

test = int(input())
while test > 0: 
    test -= 1
    print(TinhToan(input()))

        