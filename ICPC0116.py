test = int(input())
while test > 0:
    test -= 1
    number = input()
    if (int(number[0]) == int(number[len(number) - 1])): print("YES")
    else: print("NO")