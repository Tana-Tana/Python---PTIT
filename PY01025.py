xau = list(input())
for i in range(len(xau) - 3, 0,-3) :
    # print(i)
    xau.insert(i,",")
print(''.join(xau))