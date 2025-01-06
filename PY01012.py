xau_1 = input()
xau_2 = input()
p = int(input()) - 1
xau_1 = xau_1[:p] + xau_2 + xau_1[p:]
print(xau_1)