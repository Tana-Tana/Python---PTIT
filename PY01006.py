def Check(m):
    for i in range(0, len(m)):
        if m[i] != '4' and m[i] != '7':
            return False
    return True


test = int(input())
while test > 0:
    n = input()
    if Check(n) == True:
        print("YES")
    else:
        print("NO")
    test -= 1
