test = int(input())
while test > 0:
    test -= 1
    nameString = input()
    resString = ""
    cnt = 1
    for item in range(1, len(nameString)):
        if(nameString[item] != nameString[item - 1]):
            print(cnt, end='')
            print(nameString[item-1], end='')
            cnt = 1
        else:
            cnt += 1
    print(cnt, end='')
    print(nameString[len(nameString) - 1])
