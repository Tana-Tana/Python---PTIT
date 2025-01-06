def Check(number):
    # kiem tra vi tri
    for i in range(len(number)-2):
        if number[i] != number[i+2]:
            return False
    # kiem tra so khac nhau
    res = []
    for i in number:
        if (i in res) == None:
            res.append(i)
    if len(res) > 2: return False
    return True

if __name__ == "__main__":
    test = int(input())
    while test > 0:
        test -= 1
        n = input()
        if Check(n) == True: print("YES")
        else: print("NO")