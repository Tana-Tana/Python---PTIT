def STN(number):
    if len(number) <= 1: return False
    numberDao = number[::-1]
    if  numberDao != number: return False
    return True

def TinhTong(number):
    tong = 0
    for i in number:
        tong += (ord(i) - ord('0'))
    return str(tong)

if __name__ == "__main__":
    test = int(input())
    while test > 0:
        test -=1
        number = input()
        if STN(TinhTong(number)) == True: print("YES")
        else: print("NO")