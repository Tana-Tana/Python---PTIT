test = int(input())
while test > 0:
    nameString = input()
    for i in range(0, len(nameString), 2):
        a = nameString[i]
        n = int(nameString[i+1])
        for j in range(n):
            print(a, end='')
    print()
    test -= 1
