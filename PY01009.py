def Check(stringName):
    chuHoa = 0
    chuThuong = 0
    for item in stringName:
        if (item >= 'a') and (item <= 'z'): chuThuong += 1
        if (item >= 'A') and (item <= 'Z'): chuHoa += 1
    if chuThuong >= chuHoa: return stringName.lower()
    return stringName.upper()

if __name__ == '__main__':
    stringName = input()
    print(Check(stringName))
