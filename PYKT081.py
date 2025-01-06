def Check(number):
    xau = number.split('.')
    # print(xau)
    if len(xau) != 4: return False

    for i in xau:
        if i.isdigit():
            if (int(i) < 0) or (int(i) >255): return False
        else: return False
    return True

if __name__ == "__main__":
    test = int(input())
    while test > 0:
        test -=1
        number = input()
        if Check(number): print("YES")
        else: print("NO")