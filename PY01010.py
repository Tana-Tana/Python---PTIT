test = int(input())
while test > 0:
    nameString = input()
    start = nameString[0] + nameString[1]
    end = nameString[len(nameString)-2] + nameString[len(nameString)-1]
    if start == end:
        print("YES")
    else:
        print("NO")
    test -= 1
