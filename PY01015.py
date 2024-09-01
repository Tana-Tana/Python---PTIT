test = int(input())
while test > 0:
    nameString = input()
    check = False
    lenth = len(nameString)-1
    for i in range(lenth):
        if nameString[i] > nameString[i+1]:
            check = True
            break
    if check == True:
        print("NO")
    else:
        print("YES")
    test -= 1
