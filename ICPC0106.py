def cd_co_so(b, xau):
    so_bi_chia = 2
    if b == 2: return xau
    elif b == 4: so_bi_chia = 2
    elif b == 8: so_bi_chia = 3
    else: so_bi_chia = 4

    while len(xau) % so_bi_chia != 0: xau = '0' + xau
    res = ''
    for i in range(0,len(xau),so_bi_chia):
        xau_check = xau[i:i+so_bi_chia]
        number = 0
        for j in range(len(xau_check)):
            number += ((2**j) * (int(xau_check[so_bi_chia - j - 1])))
        if (number > 9): 
            number = chr(ord('A') + number - 10)
        else : number = str(number)
        res += number
    return res

# main
test = int(input())
while test > 0:
    test -= 1
    b = int(input())
    xau = input()
    print(cd_co_so(b,xau))
