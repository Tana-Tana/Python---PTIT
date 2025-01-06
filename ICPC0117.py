test = int(input())
res = []
while test > 0:
    test -= 1
    number = input()
    if res.count(number) == 0: res.append(number)
print(len(res))