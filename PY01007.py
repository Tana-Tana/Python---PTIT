import math
test = int(input())
while test > 0:
    str_number = input()
    Numbers = str_number.split()

    n = float(Numbers[0])
    x = float(Numbers[1])
    m = float(Numbers[2])

    y = float(x/100)

    resDouble = math.log(m/n, (y+1))
    resInt = math.ceil(resDouble)
    print(resInt)
    test -= 1
