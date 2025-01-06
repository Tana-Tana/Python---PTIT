def Check(number):
    for i in number:
        if (i!='0') and (i!='1') and (i!='2'): return False
    return True


if __name__ == "__main__":
    test = int(input())
    while test > 0:
        test -= 1
        n = input()
        if Check(n) == True: print("YES")
        else: print("NO")