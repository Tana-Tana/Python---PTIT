

if __name__ == "__main__":
    p = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ_.")
    while True:
        nameString = input().split()
        k = nameString[0]
        if(int(k) == 0): break
        s = nameString[1]
        # xu li
        res = []
        # print(s)
        for i in s:
            res.append(p[(p.index(i) + int(k))%28])
        # print(res)
        res = res[::-1]
        for i in res: print(i,end = '')
        print()

