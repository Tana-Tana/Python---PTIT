xau = input().split()
res = [(int(i) % 42) for i in xau]
while len(xau) < 10:
    xau1 = input().split()
    xau += xau1
    res += [(int(i)%42) for i in xau1]
s = set(res)
print(len(s))