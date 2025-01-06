xau = input()
cnt = 0
while len(xau) > 1:
    sum = 0
    for i in xau:
        sum += (ord(i) - ord('0'))
    xau = str(sum)
    cnt+=1
print(cnt)