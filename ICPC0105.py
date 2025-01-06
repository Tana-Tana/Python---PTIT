def tim_so_lon_nhat_trong_xau(xau):
    xau = list(xau)
    for i in range(len(xau)):
        if not xau[i].isdigit():
            xau[i] = str(' ')
    res = ''.join(xau)
    res = list(map(int, res.split()))
    return max(res)

# main
test = int(input())
while test > 0:
    test -= 1
    xau = input()
    print(tim_so_lon_nhat_trong_xau(xau))